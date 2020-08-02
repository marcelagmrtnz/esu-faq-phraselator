import sys
import argparse
import typing
import string
import re
import json

from nltk.translate import bleu_score
from nltk.tokenize import word_tokenize

def import_questions(filename: str) -> dict:
    with open(filename, 'r') as question_file:
        return json.load(question_file)

def select_question(asked: list, questions: dict, lang: str) -> dict:
    nested_punct = re.compile('([a-zA-Z]+)['+string.punctuation+']+([a-zA-Z]+)')
    replace = lambda match:match.group(1) + ' ' + match.group(2)
    scores = {}
    # Check here if lang is not english, then run morpheme function on asked if so.
    for i, question in questions.items():
        english, lang_b = question
        eng_q, eng_ans = list(english.items())[0]
        lang_b_q, lang_b_ans = list(lang_b.items())[0]
        
        if lang == 'english':
            hypothesis = [word.lower() for word in word_tokenize(eng_q, 'english') if word not in string.punctuation]
        else:
            # Here if possible, run lang_b_q.split() through a function that returns a list of morphemes.
            hypothesis = [word.lower() for word in lang_b_q.split() if word not in string.punctuation]

        fin_hypothesis = []
        for word in hypothesis:
            fin_hypothesis += re.sub(nested_punct, replace, word).split()

        score = bleu_score.sentence_bleu([fin_hypothesis], asked, smoothing_function=bleu_score.SmoothingFunction().method1)
        scores[i] = [score, lang_b_q, lang_b_ans, eng_q, eng_ans]

    sort_scores = sorted(scores.items(), key=lambda score:score[1][0], reverse=True)
    return sort_scores[:2]
        
def main(args):
    top_questions = select_question(args.query.split(), import_questions(args.questions), args.lang)
    print(top_questions)

if __name__ == '__main__':
    a_parser = argparse.ArgumentParser(description='Compare ASR output/queries to a pre-written FAQ to find closest two questions.')
    a_parser.add_argument('--questions', help='Use this flag to declare the FAQ file.')
    a_parser.add_argument('--query', default='', help='Use this flag to specify a query. Not using this flag results in a blank string being queried.')
    a_parser.add_argument('--lang', default='english', help='Use this flag to specify a language (yupik or english). The default is english.')
    main(a_parser.parse_args())
