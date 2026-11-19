#!/bin/sh
set -eu

repo_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
scripts_dir="$repo_dir/scripts"

case "${1:-}" in
    ''|-h|--help)
        echo "Usage: ./tool SCRIPT [ARGS...]"
        echo "Available scripts:"
        for script in "$scripts_dir"/*.py; do
            [ -f "$script" ] || continue
            name=${script##*/}
            echo "  ${name%.py}"
        done
        if [ "$#" -eq 0 ]; then exit 2; fi
        exit 0
        ;;
    *[!a-zA-Z0-9_-]*)
        echo "Invalid script name: $1" >&2
        exit 2
        ;;
esac

script="$scripts_dir/$1.py"
if [ ! -f "$script" ]; then
    echo "Unknown script: $1. Run ./tool --help for available scripts." >&2
    exit 2
fi
shift
exec python3 "$script" "$@"
