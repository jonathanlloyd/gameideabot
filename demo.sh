#!/usr/bin/env bash
cd "$(dirname "$0")"
PYTHONPATH=$PYTHONPATH:"$(pwd -P)" python ./gameideabot/idea_generator.py
