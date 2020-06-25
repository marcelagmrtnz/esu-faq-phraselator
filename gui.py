import sys
import json

import PySimpleGUI as simple
import sounddevice as sound
import subprocess
import wavio

from utils.phraselate import import_questions
from utils.phraselate import select_question

def record_query(fps):
    duration = 5.5
    query = sound.rec(int(duration*fps), samplerate=fps, channels=1)
    sound.wait()

    return query

def run_tts(filename):
    # Convert wav bits
    sox_filename = filename.split('.')[0] + '2.' + filename.split('.')[1]
    sox_command = ['sox', filename, '-b', '16', sox_filename]
    subprocess.run(sox_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Run tts with deepspeech
    command = ['deepspeech', '--model', './utils/deepspeech-0.7.3-models.pbmm', '--scorer', './utils/deepspeech-0.7.3-models.scorer', '--audio', sox_filename]
    process = subprocess.run(command, capture_output=True)
    output = process.stdout.decode()

    return output.strip()

def audio_to_question(filename, fps):
    query_audio = wavio.write(filename, record_query(fps), fps, sampwidth=3)

    query = run_tts(filename)

    # Questions format per question: [score, lang_b_q, lang_b_ans, eng_q, eng_ans]
    questions = select_question(query.split(), import_questions(sys.argv[1]))
    
    return questions

def main():
    questions = []
    with open(sys.argv[1], 'r') as question_file:
        faq = json.load(question_file)
        compiled_faq = []
        for q_num, q in faq.items():
            compiled_faq += [q_num + ') ' + list(q[0].items())[0][0]]
        faq = '\n'.join(compiled_faq)

    fps = 16000
    gui = [
    [simple.Text("Welcome! You can use this phraselator to search through the Alaska State government's frequently asked questions brochure regarding employee rights/benefits.\nThe Alaska State government's webpage where the FAQ is located can be found at https://labor.alaska.gov/lss/whfaq.htm.", font='25')],
    [simple.Text("If you aren't sure what you can ask, click here to see a listing of possible questions.", font='25'), simple.Button('Questions', font='10')],
    [simple.Text("Press the button below to record your question (in English),  and the system will find the closest question. You will have about 5 seconds to record your question.\nIf an appropriate question does not appear in the drop down once you submit, please submit again. If it does, select and confirm to receive the questions and answers.", font='25')],
    [simple.Button('Record', font='10'), simple.Text("You can also use this tool to upload a WAV file instead. There are five sample question audio files in the resources folder you can select from.", font='25'), simple.Button('Choose File', font='10')],
    [simple.Text('Please select a question...', font='25')],
    [simple.Combo([], key='questions', size=(35, 10), font='25'), simple.Button('Confirm', font='10')],
    [simple.Text("English", font='25'), simple.Text(("\t"*4)+(" "*18)+"Yup'ik", font='25')],
    [simple.Multiline("", key='english_q', size=(43, 1), font='25'), simple.Multiline("", key='langb_q', size=(43, 1), font='25')],
    [simple.Multiline("", size=(43, 5), key='english_ans', font='25'), simple.Multiline("", size=(43, 5), key='langb_ans', font='25')]
    ]

    app = simple.Window("Central Alaskan Yup'ik Phraselator", gui)
    
    while True:
        gui_event, values = app.read()
        if gui_event == simple.WIN_CLOSED:
            break
        elif gui_event == 'Record':
            questions = audio_to_question('query.wav', fps)
            app['questions'].update(values=[questions[0][1][3], questions[1][1][3]])
        elif gui_event == 'Confirm':
            for _, question in questions:
                if values['questions'] in question:
                    update_q = question
                    break
            
            app['english_q'].update(update_q[3])
            app['english_ans'].update(update_q[4])
            app['langb_q'].update(update_q[1])
            app['langb_ans'].update(update_q[2])
        elif gui_event == 'Questions':
            simple.popup_scrolled(faq, title='Question Listing', font='25')
        elif gui_event == 'Choose File':
            audio_path = simple.popup_get_file("Choose which question you'd like to test. Enter or choose any WAV file in resources.", title='Choose a WAV File', default_path='../resources/', file_types=(('WAV', '*.wav')))
            questions = audio_to_question(audio_path, fps, values['translate'])
            app['questions'].update(values=[questions[0][1][3], questions[1][1][3]])
            
    app.close()

if __name__ == '__main__':
    main()
