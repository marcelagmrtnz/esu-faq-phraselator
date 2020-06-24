import sys
import json
import numpy

def main():
    vectors = {}
    with open(sys.argv[1], 'r') as glove:
        for line in glove:
            term, vector = line.strip().split(maxsplit=1)
            # Smoothing and negative value removal
            vector = numpy.array([float(feature) for feature in vector.split()])
            vector = numpy.power(vector, 2)
            vectors[term] = numpy.add(vector, [1])
    
    with open(sys.argv[2], 'r') as dict_file:
        esu_dict = json.load(dict_file)
    
    collected = {}
    for term, term_b in esu_dict.items():
        term = term.split(';')
        vector = []
        for sub_term in term:
            vector += sub_term.split()
        vector = [term.strip().lower() for term in vector]
        
        sentence_vectors = []
        for word in vector:
            try:
                sentence_vectors.append(vectors[word])
            except:
                continue
        
        if len(sentence_vectors) > 1:
            definition = numpy.sum(sentence_vectors, axis=0)
        elif len(sentence_vectors) > 0:
            definition = numpy.array(sentence_vectors[0])
        else:
            definition = numpy.full(300, 1)
        
        
        collected[';'.join(term)] = [definition.tolist(), term_b]
    
    with open(sys.argv[3], 'w') as vector_file:
        json.dump(collected, vector_file)

main()
