#!/usr/bin/env bash
set -euo pipefail

readonly required_axm_version="0.26.2"

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

if ! command -v axm >/dev/null 2>&1; then
  echo "AXM ${required_axm_version} is required. Install it from https://axm.sh." >&2
  exit 1
fi

installed_axm_version="$(axm --version)"
if [[ "$installed_axm_version" != "$required_axm_version" ]]; then
  echo "AXM ${required_axm_version} is required; found ${installed_axm_version}." >&2
  exit 1
fi

for dependency in jq rg realpath sha256sum; do
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

validation_root="$repo_root"
if [[ "$view" == "git-index" ]]; then
  expected_index_fingerprint="$(git_index_fingerprint)"

  lint_output="$(mktemp "${TMPDIR:-/tmp}/public-safety-lint.XXXXXX")"
  snapshot_root="$(mktemp -d "${TMPDIR:-/tmp}/public-safety-git-index.XXXXXX")"
  trap 'rm -f -- "$lint_output"; cleanup' EXIT

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

  materialized_index_fingerprint="$(
    scripts/materialize-git-index.sh "$snapshot_root"
  )"
  if [[ "$materialized_index_fingerprint" != "$expected_index_fingerprint" ]]; then
    echo "The materialized snapshot does not match the Git index AXM validated." >&2
    exit 1
  fi
  assert_index_unchanged
  validation_root="$snapshot_root"
else
  axm lint --view workspace --strict
fi

expected=(
  knowledge/docs
  knowledge/field-notes
  knowledge/harness-engineering
  knowledge/workflow-automation
  packs/codebase-change-workflow
  packs/docs
  packs/effect-v4
  packs/field-notes
  packs/harness-engineering
  packs/work-management
  rules/field-notes
  skills/author-docs
  skills/author-okf
  skills/conduct-codebase-research
  skills/effect-v4-async-coordination
  skills/effect-v4-branded-types
  skills/effect-v4-config
  skills/effect-v4-error-modeling
  skills/effect-v4-observability
  skills/effect-v4-optics
  skills/effect-v4-request-batching-and-cache
  skills/effect-v4-resource-safety
  skills/effect-v4-schema-boundaries
  skills/effect-v4-services-and-layers
  skills/effect-v4-streams
  skills/effect-v4-structured-concurrency
  skills/effect-v4-testing
  skills/field-notes
  skills/frame-codebase-research
  skills/garden-context
  skills/improve-instructions
  skills/improve-whatever
  skills/plan-codebase-change
  skills/prune-work
  skills/refine-work
  skills/specify-codebase-change
  skills/temporal-dates
  skills/workshop-codebase-design
)

expected_list="$(printf '%s\n' "${expected[@]}")"
actual_list="$(
  find "$validation_root/.axm/extensions/@craigsmitham" -type f \
    \( -name skill.json -o -name pack.json -o -name knowledge.json -o -name rule.json \) \
    | sed -E "s#^${validation_root}/.axm/extensions/@craigsmitham/([^/]+/[^/]+)/.*#\\1#" \
    | sort
)"

if [[ "$expected_list" != "$actual_list" ]]; then
  echo "Public package inventory differs from the approved 38-package set." >&2
  diff <(printf '%s\n' "$expected_list") <(printf '%s\n' "$actual_list") || true
  exit 1
fi

if rg -n --hidden \
  '(/Users/|/home/[A-Za-z0-9._-]+|~/(Code|Notes|OneDrive)|agent-extensions-private|personal-os|\.exe\.xyz|craig@)' \
  "$validation_root/.axm/extensions/@craigsmitham"; then
  echo "Found a private or machine-specific identifier in public package content." >&2
  exit 1
fi

if rg -n --hidden -i \
  '(api[_-]?key|client[_-]?secret|access[_-]?token|private[_-]?key|password)[[:space:]]*[:=][[:space:]]*[^$<{[:space:]]' \
  "$validation_root/.axm/extensions/@craigsmitham"; then
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
  jq -e '
    (.description | type == "string" and length > 0) and
    (.keywords | type == "array" and length > 0) and
    (.license | type == "string" and length > 0) and
    (.homepage == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.url == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.directory | startswith(".axm/extensions/@craigsmitham/"))
  ' "$manifest" >/dev/null
done < <(find "$validation_root/.axm/extensions/@craigsmitham" -type f \
  \( -name skill.json -o -name pack.json -o -name knowledge.json -o -name rule.json \) -print0)

if jq -e '
  ([.skills | to_entries[] | select(.key != "axm") |
      (.value | if type == "object" then .source else . end)] +
   [.knowledge | to_entries[] | .value] +
   [.packs | to_entries[] | .value] +
   [.rules | to_entries[] | .value]) |
  length == 38 and
  all(type == "string" and startswith("workspace:@craigsmitham/"))
' "$validation_root/.axm/settings.json" >/dev/null; then
  :
else
  echo "A public package is not owned by this workspace." >&2
  exit 1
fi

axm knowledge lint --path "$validation_root/.axm/extensions/@craigsmitham/knowledge/docs"
axm knowledge lint --path "$validation_root/.axm/extensions/@craigsmitham/knowledge/harness-engineering"
axm knowledge lint --path "$validation_root/.axm/extensions/@craigsmitham/knowledge/workflow-automation"

if [[ "$view" == "git-index" ]]; then
  assert_index_unchanged
fi

echo "Public extension safety checks passed for the ${view} view."
