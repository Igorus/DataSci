import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    afinn_score = getTermDictionary(sent_file)
    term_score = {}
    for record in [json.loads(line) for line in tweet_file.readlines()]:
	text = record.get('text')
	if text != None:
            score = getScore(afinn_score, text)
	    words = getWords(text)
            for word in words:
                if word in term_score and len(word.strip()) > 0:
		    term_score[word][0] = term_score[word][0] + score
		    term_score[word][1] = term_score[word][1] + 1
		    term_score[word][2] = float(term_score[word][0]) /term_score[word][1]
		else:
		    term_score[word] = [score, 1, score]
    sorted_score = sorted(term_score.items(), key = lambda word: word[1][2])
    for term in sorted_score:
	print term[0], str(float(term[1][2])).encode('utf-8')
#('%.0f' % term[1][2]).rstrip('.')


def getWords(text):
    return [word.strip().encode('utf-8') for word in text.split()]                
#return [word.strip('":!@#$%^&*()_+/.,\\|?><~`][}{=-\t\n\x0b\x0c\r ').encode('utf-8') for word in text.split()]            

def getTermDictionary(sfile):
    result = {}
    for line in sfile.readlines():
	t = line.split()
	word = ' '.join(t[0:len(t)-1])
	point = int(t[len(t)-1])
	result[word] = point
    return result

def getScore(termDict, text):
    score = 0
    for word in text.split():
	w = word.strip('":!@#$%^&*()_+/.,\\|?><~`][}{=-')
	if w in termDict:
	    score = score + termDict[w]
	    #print termDict[w], ' for ', w
    return score    

if __name__ == '__main__':
    main()
