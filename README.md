# esu-faq-phraselator
Closed-domain, bidirectional FAQ search phraselator built for speech search in Central Alaskan Yup'ik and English.<br>
The GUI built for this system assumes the system is built for Central Alaskan Yup'ik, and searches an FAQ from the Alaska state government Labor Standards and Safety Division's Wage and Hour page (available [here](https://labor.alaska.gov/lss/whfaq.htm)). This system was built of previous work which can be found [here](https://github.com/marcusgabrielmartinez/faq-phraselator).

## Setup Instructions
This system has a number of dependencies. Running the following commands should take care of these in the least amount of steps.<br>
This system has only been tested on an OSX machine.
```
wget -O ./utils/deepspeech-0.7.3-models.pbmm https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm
wget -O ./utils/deepspeech-0.7.3-models.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer
virtualenv -p python3 ./env/phraselate-venv/
source ./env/phraselate-venv/bin/activate
pip3 install -r ./utils/requirements.txt
```

### Expected File Formats
- The FAQ JSON file should have the following format, and should be located in the utils subdirectory. An example is included in current utils subdirecotry.:<br>
This example FAQ file was scraped from the Alaska state government Labor Standards and Safety Division's Wage and Hour page (available [here](https://labor.alaska.gov/lss/whfaq.htm)).
```
{
'key': [
{'English Question': 'English Answer'},
{'Low-Resource Lang Question': 'Low-Resource Lang Answer'}
]
...
}
```

## Running the System
Once these commands have successfully run and the virtual environment is set up, you can run the following command to open the system's interface.<br>
Note: You must first change the file paths in the script according the provided isntructions.<br>
```
./phraselate.sh
```
If you'd like to just run the phraselator script, use the following command.<br>
```
python3 phraselate.py [--questions questions_filename] [--query "query string"]
```
- '--questions' is used to specify the FAQ filename
- '--query' is used to specify the query to be used (this is automatically filled by ASR output if the whole phraselator is used). If only phraselate.py is run, and this flag is not specified, an empty string will be queried.

## References
- [NLTK](https://www.nltk.org/)
- [sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.15/index.html)
- [wavio](https://pypi.org/project/wavio/)
- [deepspeech](https://deepspeech.readthedocs.io/en/v0.7.3/index.html)
- [deepspeech pretrained model and scorer](https://deepspeech.readthedocs.io/en/v0.7.3/USING.html)
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
- [NumPy](https://numpy.org/)
- [SciPy](https://docs.scipy.org/doc/scipy/reference/)
- [KenLM language model](https://github.com/kpu/kenlm)
- [CAY Morphological Segmenter](https://github.com/giellalt/lang-esu/tree/master)
- [CMU Wilderness fast alignments](https://github.com/festvox/datasets-CMU_Wilderness)
