# esu-faq-phraselator
Closed-domain, bidirectional FAQ search phraselator built for speech search in Central Alaskan Yup'ik and English.<br>
The GUI built for this system assumes the system is built for Central Alaskan Yup'ik, and searches an FAQ from the Alaska state government Labor Standards and Safety Division's Wage and Hour page (available [here](https://labor.alaska.gov/lss/whfaq.htm)).<br>
This was built as part of a graduate-level capstone project at the University of Washington, Summer 2020, and built on previous work completed as part of a graduate-level course at the University of Washington, Spring 2020.
- Spring 2020: LING 575- Speech Technology for Endangered Languages (Prof: Dr. Gina-Anne Levow)
- Summer 2020: LING 600- Capstone Project (Advisor: Dr. Gina-Anne Levow)

## Setup Instructions
This system has a number of dependencies. Running the following commands should take care of these in the least amount of steps.<br>
This system has only been tested on an OSX machine.
```
./models.sh
python3 -m venv ./env/phraselate-venv/
source ./env/phraselate-venv/bin/activate
./dependencies.sh
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
```
./phraselate.sh
```
You can switch which instance of gui.py is called within phraselate.sh by commenting one of the lines out. Leave the line with '--debug' uncommented to have deepspeech stderr and stdout printed.<br>
If you'd like to just run the phraselator script, use the following command.<br>
```
python3 phraselate.py [--questions questions_filename] [--query "query string"] [--lang english | yupik]
```
- '--questions' is used to specify the FAQ filename
- '--query' is used to specify the query to be used (this is automatically filled by ASR output if the whole phraselator is used). If only phraselate.py is run, and this flag is not specified, an empty string will be queried.
- '--lang' is used to specify the language to search with (yupik or english). The default is English.

## Yup'ik Models
The Yup'ik acoutic and language models were built using Mozilla's DeepSpeech framework. The model is based on Mozilla's standard English acoustic model, and fine-tuned with Yup'ik acoustic data (cited below, in addition to data collected from a heritage Yup'ik speaker). The acoustic model was fine-tuned for 653 epochs. The langauge model was built using DeepSpeech's KenLM langauge model builder (referred to by DeepSpeech as a 'scorer').

## Results

### DeepSpeech Model
The model achieves the following results, with the scorer enabled.<br>
Average WER- 0.496

### Overall Sytem
The overall search system achieves the following results.<br>
English search- 0.391<br>
Yup'ik search- 0.848<br>
Note: Testing for these results utilized the same speakers used in training, so the system is likely very speaker-dependent. In addition, it is certainly closed-domain. Overall system results were tested without live recording, and results can vary widely depending on hardware used to record, etc.

## Data Sources
- [Alaska Employees FAQ](https://labor.alaska.gov/lss/whfaq.htm)
- [The Sound of Central Alaskan Yup'ik (Numbers, Phrases, & Sample Text)](https://www.youtube.com/watch?v=ugkchkfp6dQ)
- [Yup'ik Eskimo Dictionary, S. Jacobson](https://www.uaf.edu/danl/project-updates/steven-jacobson/)
- [American Bible Society, Yup'ik Bible Translation](https://www.americanbible.org/)

## References
- [NLTK](https://www.nltk.org/)
- [sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.15/index.html)
- [wavio](https://pypi.org/project/wavio/)
- [deepspeech](https://deepspeech.readthedocs.io/en/v0.7.3/index.html)
- [deepspeech pretrained model and scorer](https://deepspeech.readthedocs.io/en/v0.7.3/USING.html)
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
- [pydub](https://github.com/jiaaro/pydub/blob/master/API.markdown)
- [NumPy](https://numpy.org/)
- [SciPy](https://docs.scipy.org/doc/scipy/reference/)
- [KenLM language model](https://github.com/kpu/kenlm)
