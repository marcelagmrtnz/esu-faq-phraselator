import json
import sys

def main():
    esu_dict = {}
    with open(sys.argv[1], 'r') as dict_file:
        for line in dict_file:
            term = list(json.loads(line).values())[0][0]
            if len(term) > 1:
                esu_dict[';'.join(term[1])] = term[0][0]
            else:
                esu_dict[term[1]] = term[0][0]

    with open(sys.argv[2], 'w') as term_file:
        json.dump(esu_dict, term_file)

main()
