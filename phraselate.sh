#!/bin/sh

## Run these commands before running this script.
# virtualenv -p python3 ./env/phraselate-venv/
# source ./env/phraselate-venv/bin/activate
# pip3 install -r ./utils/requirements.txt

## Change the pathnames in '## pathname ##' below before running to the appropriate files.

if [ ! -f "./utils/pickled_B.glove.6B.300d.txt" ]; then 
    python3 pickle_vectors.py ## Filename of output ## ## Path to 300d GloVe vectors ##
fi
python3 gui.py ## Path to output of collect_vectors.py ## ## Path to output of pickle_vectors.py ##  ## Path to FAQ file ##
rm -f *.wav
rm -rf __pycache__/
