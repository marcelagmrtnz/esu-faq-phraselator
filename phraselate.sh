#!/bin/sh

## Run these commands before running this script.
# ./downloads.sh
# python3 -m venv ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# ./dependencies.sh

python3 gui.py ./utils/questions.json
#python3 gui.py ./utils/questions.json --debug
rm -f *.wav
rm -rf utils/__pycache__/
