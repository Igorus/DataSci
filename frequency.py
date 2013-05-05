import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    all_terms = 0
    term_score = {}
    for record in [json.loads(line) for line in tweet_file.readlines()]:
	text = record.get('text')
	if text != None:
            words = getWords(text)
            for word in words:
                if word in term_score and len(word) > 0:
		    term_score[word] = term_score[word] + 1
                    all_terms += 1
		else:
		    term_score[word] = 1
                    all_terms += 1
    
    sorted_score = sorted(term_score.items(), key = lambda word: word[1])
    for word in sorted_score:
	print word[0], float(word[1]) / all_terms


def getWords(text):
    return [word.strip().encode('utf-8') for word in text.split()]

if __name__ == '__main__':
    main()
