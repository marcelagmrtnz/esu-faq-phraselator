# faq-phraselator
Closed-domain, asymmetric FAQ search phraselator.<br>
The GUI built for this system assumes the system is built for Central Alaskan Yup'ik, and searches an FAQ from the Alaska state government Labor Standards and Safety Division's Wage and Hour page (available [here](https://labor.alaska.gov/lss/whfaq.htm)). However, this system could in theory be adjsuted to work for any FAQ/low-resource language.

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
## Preprocessing
The base system expects files in a certain format. Scripts are provided to achieve these formats given a JSON dictionary and JSON question file is started with.<br>
The scripts should be run in the following order, and should output in the utils subdirectory to function correctly.<br>
```
python3 process_dict.py [original_dictionary_filename] [output_filename]
python3 collect_vectors.py [300d GloVe vectors] [processed_dictionary_filename] [output_filename]
python3 pickle_vectors.py [output_filename] [300d GloVe vectors]
```

### Expected File Formats
- process_dict.py expects a JSON file with the following format:<br>
```
...
{'key': [[['term'], ['translation_1', 'translation_2', ...]]], ...}
...
```
- collect_vectors.py expects a JSON file with the following format (should be output by process_dict.py):<br>
```
{
{'tranlsation_1;translation_2;...': 'term'},
...
}
```
...as well as the standard 300d 6B release of English Wikipedia GloVe vectors.<br>
- pickle_vectors.py expects only the standard 300d 6B release of English Wikipedia GloVe vectors.<br>
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
If you'd like to just run the phraselator script, use the following commands.<br>
This command corresponds to the search by translation system.<br>
```
python3 phraselate.py --dictionary [collected_vectors_filename] --questions [questions_filename] --vectors [pickled_glove_vectors] --translate
```
This command corresponds to the search by English system.<br>
```
python3 phraselate.py --dictionary [collected_vectors_filename] --questions [questions_filename] --vectors [pickled_glove_vectors]
```

## References
- [NLTK](https://www.nltk.org/)
- [sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.15/index.html)
- [wavio](https://pypi.org/project/wavio/)
- [deepspeech](https://deepspeech.readthedocs.io/en/v0.7.3/index.html)
- [deepspeech pretrained model and scorer](https://deepspeech.readthedocs.io/en/v0.7.3/USING.html)
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
- [NumPy](https://numpy.org/)
- [SciPy](https://docs.scipy.org/doc/scipy/reference/)
- [English Wikipedia GloVe vectors](https://nlp.stanford.edu/projects/glove/)
