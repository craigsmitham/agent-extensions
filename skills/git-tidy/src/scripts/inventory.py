"""Print read-only Git facts for one repository, including linked checkouts."""

import json
import os
import socket
import subprocess
import sys


def git(path, *args):
    result = subprocess.check_output(
        ["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", path, *args]
    )
    return os.fsdecode(result)


def inventory(path):
    common = git(path, "rev-parse", "--path-format=absolute", "--git-common-dir").removesuffix("\n")
    branches = []
    for row in git(path, "for-each-ref", "--format=%(refname)%00%(objectname)%00%(upstream)%00%(upstream:track,nobracket)", "refs/heads").splitlines():
        ref, tip, upstream, tracking = row.split("\0")
        branches.append(dict(ref=ref, tip=tip, upstream=upstream, tracking=tracking))

    worktrees = []
    for block in git(path, "worktree", "list", "--porcelain", "-z").split("\0\0"):
        if not block:
            continue
        fields = {}
        for item in block.rstrip("\0").split("\0"):
            key, _, value = item.partition(" ")
            fields[key] = value
        checkout = fields["worktree"]
        if "bare" not in fields and "prunable" not in fields:
            try:
                actual = git(checkout, "rev-parse", "--show-toplevel").removesuffix("\n")
                owner = git(checkout, "rev-parse", "--path-format=absolute", "--git-common-dir").removesuffix("\n")
                if not os.path.samefile(actual, checkout) or not os.path.samefile(owner, common):
                    raise ValueError("worktree identity changed")
                status = git(checkout, "status", "--porcelain=v1", "-z", "--untracked-files=normal",
                             "--ignored=matching", "--ignore-submodules=none", "--no-renames")
                fields["status_codes"] = sorted({entry[:2] for entry in status.split("\0") if entry})
            except (OSError, ValueError, subprocess.CalledProcessError) as exc:
                fields["inspection_error"] = str(exc)
        worktrees.append(fields)

    stashes = []
    for row in git(path, "stash", "list", "--format=%H%x00%gd%x00%ci%x00%gs").splitlines():
        oid, selector, date, subject = row.split("\0", 3)
        stashes.append(dict(oid=oid, selector=selector, date=date, subject=subject))
    return dict(host=socket.gethostname(), common_dir=common, branches=branches,
                worktrees=worktrees, stashes=stashes)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 inventory.py REPOSITORY")
    print(json.dumps(inventory(sys.argv[1]), indent=2))
