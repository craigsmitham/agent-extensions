#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

axm lint --strict

expected=(
  knowledge/docs
  packs/docs
  packs/effect-v4
  skills/author-guide
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
  skills/eval-whatever
  skills/okf-author
  skills/review-docs
  skills/temporal-dates
)

expected_list="$(printf '%s\n' "${expected[@]}")"
actual_list="$(
  find .axm/extensions/@craigsmitham -type f \
    \( -name skill.json -o -name pack.json -o -name knowledge.json \) \
    | sed -E 's#^.axm/extensions/@craigsmitham/([^/]+/[^/]+)/.*#\1#' \
    | sort
)"

if [[ "$expected_list" != "$actual_list" ]]; then
  echo "Public package inventory differs from the approved 21-package set." >&2
  diff <(printf '%s\n' "$expected_list") <(printf '%s\n' "$actual_list") || true
  exit 1
fi

if rg -n --hidden \
  '(/Users/|/home/[A-Za-z0-9._-]+|~/(Code|Notes|OneDrive)|agent-extensions-private|personal-os|\.exe\.xyz|craig@)' \
  .axm/extensions/@craigsmitham; then
  echo "Found a private or machine-specific identifier in public package content." >&2
  exit 1
fi

if rg -n --hidden -i \
  '(api[_-]?key|client[_-]?secret|access[_-]?token|private[_-]?key|password)[[:space:]]*[:=][[:space:]]*[^$<{[:space:]]' \
  .axm/extensions/@craigsmitham; then
  echo "Found a possible hard-coded secret in public package content." >&2
  exit 1
fi

while IFS= read -r link; do
  resolved="$(realpath "$link")"
  case "$resolved" in
    "$repo_root"/*) ;;
    *)
      echo "Symlink escapes repository: $link -> $resolved" >&2
      exit 1
      ;;
  esac
done < <(find . -path ./.git -prune -o -type l -print)

while IFS= read -r manifest; do
  jq -e '
    (.description | type == "string" and length > 0) and
    (.keywords | type == "array" and length > 0) and
    (.license | type == "string" and length > 0) and
    (.homepage == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.url == "https://github.com/craigsmitham/agent-extensions") and
    (.repository.directory | startswith(".axm/extensions/@craigsmitham/"))
  ' "$manifest" >/dev/null
done < <(find .axm/extensions/@craigsmitham -type f \
  \( -name skill.json -o -name pack.json -o -name knowledge.json \))

if jq -e '
  ([.skills | to_entries[] | select(.key != "axm") | .value] +
   [.knowledge | to_entries[] | .value] +
   [.packs | to_entries[] | .value]) |
  length == 21 and
  all(type == "string" and startswith("workspace:@craigsmitham/"))
' .axm/settings.json >/dev/null; then
  :
else
  echo "A public package is not owned by this workspace." >&2
  exit 1
fi

axm knowledge lint --path .axm/extensions/@craigsmitham/knowledge/docs

echo "Public extension safety checks passed."
