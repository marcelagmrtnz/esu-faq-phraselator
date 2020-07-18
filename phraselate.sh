#!/bin/sh

## Run these commands before running this script.
# virtualenv -p python3 ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# pip3 install -r ./utils/requirements.txt

python3 gui.py ./utils/questions.json
rm -f *.wav
rm -rf utils/__pycache__/
