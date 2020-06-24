import pickle
import numpy
import sys

def import_vectors():
    vectors = {}
    with open(sys.argv[2], 'r') as glove:
        for line in glove:
            term, vector = line.strip().split(maxsplit=1)
            # Smoothing and negative value removal
            vector = numpy.array([float(feature) for feature in vector.split()])
            vector = numpy.power(vector, 2)
            vectors[term] = numpy.add(vector, [1])
    
    return vectors

def main():
    with open(sys.argv[1], 'wb') as pickle_file:
        pickle.dump(import_vectors(), pickle_file)

main()
