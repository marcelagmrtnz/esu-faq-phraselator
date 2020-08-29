#!/bin/sh

### Run this file to download models ###

## Download English acoustic/language models
wget -O ./utils/deepspeech-0.7.3-models.pbmm https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm
wget -O ./utils/deepspeech-0.7.3-models.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer

# Reconstruct Yup'ik acoustic/language models
cat utils/esu_models/* > utils/esu_models.tar.gz
tar -xzf utils/esu_models.tar.gz
mv esu_models/* utils/
rm -rf esu_models/; rm -rf utils/esu_models/;
rm utils/esu_models.tar.gz

## Instruct to create and source virtual environment
echo "DONE! Run the following commands next:"
echo "python3 -m venv ./env/phraselate-venv/"
echo "source ./env/phraselate-venv/bin/activate"
echo "./dependencies.sh"

