import sys
import json

def countTags(lines):
    dictionary = {}
    for jline in [json.loads(line) for line in lines]:
	entities = jline.get('entities')
	if not(entities is None) :
	    hashtags = entities.get('hashtags')
	    if len(hashtags) > 0 :
		for hashtag in hashtags:
		    if len(hashtag) > 0:
			tag = hashtag.get('text')
			if tag in dictionary:
			    dictionary[tag] = dictionary[tag] + 1
			else:
			    dictionary[tag] = 1;
    top = sorted(dictionary.items(), key = lambda word: word[1], reverse=True)
    for word in top[0:10]:
	print word[0], ' ', float(word[1])
		
def main():
    tweet_file = open(sys.argv[1])
    countTags(tweet_file.readlines())
    


if __name__ == '__main__':
    main()
