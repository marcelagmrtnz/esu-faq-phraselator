#!/bin/sh

## Run these commands before running this script.
# wget -O ./utils/deepspeech-0.7.3-models.pbmm https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm
# wget -O ./utils/deepspeech-0.7.3-models.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer
# virtualenv -p python3 ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# pip3 install -r ./utils/requirements.txt

# Add download for punkt tokenizer
# Add download for esu models

python3 gui.py ./utils/questions.json
rm -f *.wav
rm -rf utils/__pycache__/
