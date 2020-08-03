#!/bin/sh

## Install dependencies
pip3 install -r ./utils/requirements.txt
python3 -c "import nltk; nltk.download('punkt');"

echo "DONE!"
