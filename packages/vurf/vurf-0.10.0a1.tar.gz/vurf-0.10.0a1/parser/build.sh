#!/usr/bin/env bash

set -e
set -u
set -x

DIR=$(dirname "$0")
PARSER_FILE="$DIR/stand_alone.py"

rm "$PARSER_FILE"
poetry run python -m lark.tools.standalone "$DIR/grammar.lark" > "$PARSER_FILE"
