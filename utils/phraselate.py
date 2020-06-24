import sys
import argparse
import typing
import string
import re
import json
import pickle

import numpy
from scipy.spatial import distance
from nltk.metrics.distance import edit_distance
from nltk.translate import bleu_score
from nltk.tokenize import word_tokenize

def import_vectors(filename: str) -> dict:
    with open(filename, 'rb') as pickled_vectors:
        vectors = pickle.load(pickled_vectors)

    return vectors

def import_dict(filename: str) -> dict:
    with open(filename, 'r') as term_dict:
        temp_dict = json.load(term_dict)
        esu_dict = {}
        for term, vector in temp_dict.items():
            esu_dict[term] = [numpy.array([float(feature) for feature in vector[0]]), vector[1]]

    return esu_dict

def import_questions(filename: str) -> dict:
    with open(filename, 'r') as question_file:
        return json.load(question_file)

def term_lookup(search_term: str, esu_dict: dict) -> str:
    comparisons = {}
    for term in esu_dict:
        comparisons[distance.cosine(esu_dict[term][0], search_term)] = esu_dict[term]
    return min(comparisons.items(), key=lambda term:term[0])[1][1]

def translate(sent: list, esu_dict: dict, vectors: dict) -> list:
    translation = []
    for term in sent:
        try:
            term = vectors[term]
        except:
            term = numpy.zeros(300)

        translation.append(term_lookup(term, esu_dict))
    return translation

def select_question(asked: list, questions: dict, translate=True) -> dict:
    nested_punct = re.compile('([a-zA-Z]+)['+string.punctuation+']+([a-zA-Z]+)')
    replace = lambda match:match.group(1) + ' ' + match.group(2)
    scores = {}
    if translate:
        for i, question in questions.items():
            english, lang_b = question
            eng_q, eng_ans = list(english.items())[0]
            lang_b_q, lang_b_ans = list(lang_b.items())[0]

            hypothesis = [word.lower() for word in lang_b_q.split() if word not in string.punctuation]
            fin_hypothesis = []
            for word in hypothesis:
                fin_hypothesis += re.sub(nested_punct, replace, word).split()

            score = edit_distance(' '.join(fin_hypothesis), ' '.join(asked).lower())
            #score = bleu_score.sentence_bleu([fin_hypothesis], asked, smoothing_function=bleu_score.SmoothingFunction().method1)
            scores[i] = [score, lang_b_q, lang_b_ans, eng_q, eng_ans]
    else:
        for i, question in questions.items():
            english, lang_b = question
            eng_q, eng_ans = list(english.items())[0]
            lang_b_q, lang_b_ans = list(lang_b.items())[0]

            hypothesis = [word.lower() for word in word_tokenize(eng_q, 'english') if word not in string.punctuation]
            fin_hypothesis = []
            for word in hypothesis:
                fin_hypothesis += re.sub(nested_punct, replace, word).split()

            score = bleu_score.sentence_bleu([fin_hypothesis], asked, smoothing_function=bleu_score.SmoothingFunction().method1)
            scores[i] = [score, lang_b_q, lang_b_ans, eng_q, eng_ans]

    sort_scores = sorted(scores.items(), key=lambda score:score[1][0], reverse=True)
    return sort_scores[:2]
        

def main(args):
    if args.translate:
        translation = translate(['minimum', 'wage'], import_dict(args.dictionary), import_vectors(args.vectors))
        top_questions = select_question(translation, import_questions(args.questions))
    else:
        top_questions = select_question(['on', 'call'], import_questions(args.questions), translate=False)
    
    print(top_questions)

if __name__ == '__main__':
    a_parser = argparse.ArgumentParser(description='handles method')
    a_parser.add_argument('--translate', action='store_true')
    a_parser.add_argument('--dictionary', default='')
    a_parser.add_argument('--questions')
    a_parser.add_argument('--vectors')
    main(a_parser.parse_args())
