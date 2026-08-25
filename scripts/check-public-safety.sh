#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 [--view workspace|git-index]" >&2
}

view="workspace"
if [[ $# -gt 0 ]]; then
  if [[ $# -ne 2 || "$1" != "--view" ]]; then
    usage
    exit 2
  fi
  view="$2"
fi

if [[ "$view" != "workspace" && "$view" != "git-index" ]]; then
  usage
  exit 2
fi

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"
trusted_eval_validator="$repo_root/agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/scripts/agent-skill-eval.mjs"

if ! command -v axm >/dev/null 2>&1; then
  echo "AXM is required. Install the latest release from https://axm.sh." >&2
  exit 1
fi

for dependency in jq node rg realpath sha256sum; do
  if ! command -v "$dependency" >/dev/null 2>&1; then
    echo "The public safety gate requires '$dependency', but it is not installed." >&2
    exit 1
  fi
done

git_index_fingerprint() {
  local digest
  digest="$(git ls-files --stage -z | sha256sum | cut -d ' ' -f 1)"
  printf 'sha256:%s\n' "$digest"
}

assert_index_unchanged() {
  local current_fingerprint
  current_fingerprint="$(git_index_fingerprint)"
  if [[ "$current_fingerprint" != "$expected_index_fingerprint" ]]; then
    echo "The Git index changed during public safety validation; rerun the commit." >&2
    exit 1
  fi
}

snapshot_root=""
cleanup() {
  if [[ -n "$snapshot_root" ]]; then
    rm -rf -- "$snapshot_root"
  fi
}
trap cleanup EXIT

assert_sync_converged() {
  local root="$1"
  local output="$2"

  if ! (cd "$root" && axm sync --preview --json) >"$output"; then
    cat "$output"
    return 1
  fi

  if ! jq -e '
    select(
      .ok == true and
      (.result.outcome == "previewed" or .result.outcome == "no-op") and
      .result.counts.failed == 0 and
      .result.counts.blocked == 0
    )
  ' "$output" >/dev/null; then
    cat "$output"
    echo "AXM sync preview did not report a recoverable workspace." >&2
    return 1
  fi
}

validation_root="$repo_root"
if [[ "$view" == "git-index" ]]; then
  expected_index_fingerprint="$(git_index_fingerprint)"

  sync_output="$(mktemp "${TMPDIR:-/tmp}/public-safety-sync.XXXXXX")"
  lint_output="$(mktemp "${TMPDIR:-/tmp}/public-safety-lint.XXXXXX")"
  snapshot_root="$(realpath "$(mktemp -d "${TMPDIR:-/tmp}/public-safety-git-index.XXXXXX")")"
  trap 'rm -f -- "$sync_output" "$lint_output"; cleanup' EXIT

  materialized_index_fingerprint="$(
    scripts/materialize-git-index.sh "$snapshot_root"
  )"
  if [[ "$materialized_index_fingerprint" != "$expected_index_fingerprint" ]]; then
    echo "The materialized snapshot does not match the Git index." >&2
    exit 1
  fi
  assert_index_unchanged
  validation_root="$snapshot_root"

  if ! assert_sync_converged "$validation_root" "$sync_output"; then
    exit 1
  fi
  assert_index_unchanged

  if ! axm lint --view git-index --strict --json >"$lint_output"; then
    cat "$lint_output"
    exit 1
  fi

  reported_index_fingerprint="$(
    jq -er '
      select(.ok == true and .result.input.view == "git-index") |
      .result.input.fingerprint
    ' "$lint_output"
  )"
  if [[ "$reported_index_fingerprint" != "$expected_index_fingerprint" ]]; then
    echo "AXM validated a different Git index; rerun the commit." >&2
    exit 1
  fi
  assert_index_unchanged
else
  sync_output="$(mktemp "${TMPDIR:-/tmp}/public-safety-sync.XXXXXX")"
  trap 'rm -f -- "$sync_output"; cleanup' EXIT
  assert_sync_converged "$validation_root" "$sync_output"
  axm lint --view workspace --strict
fi

authored_roots=(
  "$validation_root/knowledge"
  "$validation_root/packs"
  "$validation_root/rules"
  "$validation_root/skills"
  "$validation_root/subagents"
)

find_authored_manifests() {
  find "${authored_roots[@]}" -type f \
    \( -name skill.json -o -name subagent.json -o -name pack.json -o -name knowledge.json -o -name rule.json \) \
    "$@"
}

expected=(
  knowledge/docs
  knowledge/effect-v4
  knowledge/field-notes
  knowledge/gen-stack
  knowledge/knowledge-management
  knowledge/product-management
  knowledge/software-architecture
  knowledge/software-engineering
  knowledge/strategy
  knowledge/workflow-automation
  packs/docs
  packs/effect-v4
  packs/field-notes
  packs/gen-stack
  packs/qrspi
  packs/software-architecture
  packs/software-engineering
  rules/field-notes
  rules/tidy-first
  rules/use-effect-v4
  rules/yagni
  skills/audit-docs
  skills/author-architecture-docs
  skills/author-docs
  skills/author-okf
  skills/author-software-work-items
  skills/craft-effect-v4
  skills/field-notes
  skills/improve-whatever
  skills/question
  skills/reconcile-architecture-docs
  skills/research
  skills/setup-architecture-docs
  skills/temporal-dates
  subagents/researcher
)

expected_list="$(printf '%s\n' "${expected[@]}")"
actual_list="$(
  find_authored_manifests \
    | sed -E "s#^${validation_root}/([^/]+/[^/]+)/.*#\\1#" \
    | sort
)"

if [[ "$expected_list" != "$actual_list" ]]; then
  echo "Public package inventory differs from the approved ${#expected[@]}-package set." >&2
  diff <(printf '%s\n' "$expected_list") <(printf '%s\n' "$actual_list") || true
  exit 1
fi

while IFS= read -r -d '' manifest; do
  package_root="$(dirname "$manifest")"
  if ! node "$trusted_eval_validator" validate \
    --root "$validation_root" \
    --package "${package_root#"$validation_root/"}"; then
    echo "Agent Skill evaluation source does not conform to repository policy." >&2
    exit 1
  fi
done < <(find "$validation_root/skills" -mindepth 2 -maxdepth 2 -name skill.json -print0)

if rg -n --hidden \
  '(/Users/|/home/[A-Za-z0-9._-]+|~/(Code|Notes|OneDrive)|agent-extensions-private|personal-os|\.exe\.xyz|craig@)' \
  "${authored_roots[@]}"; then
  echo "Found a private or machine-specific identifier in public package content." >&2
  exit 1
fi

if rg -n --hidden -i \
  '(api[_-]?key|client[_-]?secret|access[_-]?token|private[_-]?key|password)[[:space:]]*[:=][[:space:]]*[^$<{[:space:]]' \
  "${authored_roots[@]}"; then
  echo "Found a possible hard-coded secret in public package content." >&2
  exit 1
fi

while IFS= read -r -d '' link; do
  resolved="$(realpath "$link")"
  case "$resolved" in
    "$validation_root"/*) ;;
    *)
      echo "Symlink escapes validation root: $link -> $resolved" >&2
      exit 1
      ;;
  esac
done < <(find "$validation_root" -path "$validation_root/.git" -prune -o -type l -print0)

while IFS= read -r -d '' manifest; do
  relative_manifest="${manifest#"$validation_root/"}"
  expected_directory="$(dirname "$relative_manifest")"
  jq -e --arg expected_directory "$expected_directory" '
    (.description | type == "string" and length > 0) and
    (.keywords | type == "array" and length > 0) and
    (.license | type == "string" and length > 0) and
    (.homepage == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.url == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.directory == $expected_directory)
  ' "$manifest" >/dev/null
done < <(find_authored_manifests -print0)

while IFS= read -r license_id; do
  if [[ ! -f "$validation_root/LICENSES/${license_id}.txt" ]]; then
    echo "Missing license text for declared SPDX identifier: ${license_id}" >&2
    exit 1
  fi
done < <(
  find_authored_manifests -print0 \
    | xargs -0 jq -r '.license' \
    | rg -o '[A-Za-z0-9][A-Za-z0-9.-]*' \
    | rg -v '^(AND|OR|WITH)$' \
    | sort -u
)

if jq -e --argjson expected_count "${#expected[@]}" '
  def source:
    if type == "object" and .source == "workspace" and .origin == "bundled"
    then "bundled"
    elif type == "object" then .source
    else .
    end;
  ([
    (.skills | to_entries[] | {type: "skills", key, source: (.value | source)}),
    (.knowledge | to_entries[] | {type: "knowledge", key, source: (.value | source)}),
    (.packs | to_entries[] | {type: "packs", key, source: (.value | source)}),
    (.rules | to_entries[] | {type: "rules", key, source: (.value | source)}),
    (.subagents | to_entries[] | {type: "subagents", key, source: (.value | source)})
  ]) as $entries |
  ([$entries[] | select(.source == "workspace")] |
    length == $expected_count) and
  all($entries[];
    (.source == "workspace") or
    (.type == "skills" and .key == "axm" and
      ((.source | startswith("agentxm:@agentxm/skills/axm")) or
       .source == "bundled")) or
    (.type == "packs" and
      (.key == "agent-engineering" or
       .key == "context-engineering" or
       .key == "harness-engineering" or
       .key == "skill-engineering") and
      .source == ("agentxm:@agentxm/packs/" + .key))
  )
' "$validation_root/axm.json" >/dev/null; then
  :
else
  echo "The workspace contains an unexpected package owner or source." >&2
  exit 1
fi

while IFS= read -r -d '' manifest; do
  axm knowledge lint --path "$(dirname "$manifest")"
done < <(find "$validation_root/knowledge" \
  -mindepth 2 -maxdepth 2 -name knowledge.json -print0)

if [[ "$view" == "git-index" ]]; then
  assert_index_unchanged
fi

echo "Public extension safety checks passed for the ${view} view."
