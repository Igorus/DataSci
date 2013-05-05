import sys
import json

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

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    TermDict = getTermDictionary(sent_file)
    for record in [json.loads(line) for line in tweet_file.readlines()]:
	text = record.get('text')
	if text != None:
	    print float(getScore(TermDict, text))

if __name__ == '__main__':
    main()
