#!/bin/sh

### Run this file to download models ###

## Download English/esu acoustic/language models
wget -O ./utils/deepspeech-0.7.3-models.pbmm https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm
wget -O ./utils/deepspeech-0.7.3-models.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer
wget -O ./utils/esu_model_500epochs.pbmm https://www.dropbox.com/s/4ztgn4vvwoglo71/esu_model_500epochs.pbmm?raw=0
wget -O ./utils/esu_lm.scorer https://www.dropbox.com/s/09tbeqs4xzlkmaj/esu_lm.scorer?raw=0

## Instruct to create and source virtual environment
echo "DONE! Run the following commands next:"
echo "python3 -m venv ./env/phraselate-venv/"
echo "source ./env/phraselate-venv/bin/activate"
echo "./dependencies.sh"

