#!/bin/sh

## Run these commands before running this script.
# wget -O ./utils/deepspeech-0.7.3-models.pbmm https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm
# wget -O ./utils/deepspeech-0.7.3-models.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer
# wget -O ./utils/esu_model_500epochs.pbmm https://www.dropbox.com/s/4ztgn4vvwoglo71/esu_model_500epochs.pbmm?raw=0
# wget -O ./utils/esu_lm.scorer https://www.dropbox.com/s/09tbeqs4xzlkmaj/esu_lm.scorer?raw=0
# virtualenv -p python3 ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# pip3 install -r ./utils/requirements.txt

python3 gui.py ./utils/questions.json
rm -f *.wav
rm -rf utils/__pycache__/
