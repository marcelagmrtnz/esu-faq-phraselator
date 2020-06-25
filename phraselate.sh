#!/bin/sh

## Run these commands before running this script.
# virtualenv -p python3 ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# pip3 install -r ./utils/requirements.txt

## Change the pathnames in '## pathname ##' below before running to the appropriate files.

python3 gui.py ./utils/questions.json
rm -f *.wav
rm -rf utils/__pycache__/
