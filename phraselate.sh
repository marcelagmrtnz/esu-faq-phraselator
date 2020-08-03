#!/bin/sh

## Run install.sh before running this script.

python3 gui.py ./utils/questions.json
rm -f *.wav
rm -rf utils/__pycache__/
