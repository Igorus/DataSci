import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    TermDict = getTermDictionary(sent_file)

    state_score = {} #State_Name: {# of happy, # of sad, #no mood}
    for record in [json.loads(line) for line in tweet_file.readlines()]:
	state = getState(record)
	if state != None:
            text = record.get('text')
	    if text != None:
	        score = getScore(TermDict, text)

		if state not in state_score:
		    state_score[state] = {}
		    state_score[state]['happy'] = 0
		    state_score[state]['sad'] = 0
		    state_score[state]['nomood'] = 0			

 	        if score > 0:
		    state_score[state]['happy'] += 1
                elif score < 0:
		    state_score[state]['sad'] += 1
		else :
		    state_score[state]['nomood'] += 1
    #print state_score

    def calc(state):
        return float(state['happy'] - state['sad']) / (state['happy'] + state['sad'] + state['nomood'])

    sorted_score = sorted(state_score.items(), key = lambda state: calc(state[1]))
    #for state in sorted_score:
    #	print state[0], float(calc(state[1])), state_code[state[0]]
    print state_code[sorted_score[-1][0]]

def getState(record):
    place = record.get('place')
    if place != None:
	if place.get('country_code') == u'US': 
	    if place.get('place_type') == 'admin':
	        return place.get('name')
    else: return None

def getWords(text):
    return [word.strip().encode('utf-8') for word in text.split()]

def getScore(termDict, text):
    score = 0
    for word in text.split():
	w = word.strip('":!@#$%^&*()_+/.,\\|?><~`][}{=-')
	if w in termDict:
	    score = score + termDict[w]
	    #print termDict[w], ' for ', w
    return score

def getTermDictionary(sfile):
    result = {}
    for line in sfile.readlines():
	t = line.split()
	word = ' '.join(t[0:len(t)-1])
	point = int(t[len(t)-1])
	result[word] = point
    return result


state_code = {
'Alabama'               : 'AL',
'Alaska'                : 'AK',
'Arizona'               : 'AZ',
'Arkansas'             : 'AR',
'California'         : 'CA',
'Colorado'             : 'CO',
'Connecticut'         : 'CT',
'Delaware'             : 'DE',
'District of Columbia'  : 'DC',
'Florida'             : 'FL',
'Georgia'             : 'GA',
'Hawaii'             : 'HI',
'Idaho'                 : 'ID',
'Illinois'              : 'IL',
'Indiana'             : 'IN',
'Iowa'                 : 'IA',
'Kansas'             : 'KS',
'Kentucky'              : 'KY',
'Louisian'              : 'LA',
'Maine'                 : 'ME',
'Maryland'              : 'MD',
'Massachusetts'         : 'MA',
'Michigan'             : 'MI',
'Minnesota'             : 'MN',
'Mississippi'         : 'MS',
'Missouri'             : 'MO',
'Montana'               : 'MT',
'Nebraska'              : 'NE',
'Nevada'                : 'NV',
'New Hampshire'         : 'NH',
'New Jersey'            : 'NJ',
'New Mexico'            : 'NM',
'New York'             : 'NY',
'North Carolina'        : 'NC',
'North Dakota'         : 'ND',
'Ohio'                  : 'OH',
'Oklahoma'              : 'OK',
'Oregon'                : 'OR',
'Pennsylvania'         : 'PA',
'Rhode Island'         : 'RI',
'South Carolina'     : 'SC',
'South Dakota'         : 'SD',
'Tennessee'             : 'TN',
'Texas'                 : 'TX',
'Utah'                 : 'UT',
'Vermont'             : 'VT',
'Virginia'              : 'VA',
'Washington'            : 'WA',
'West Virginia'         : 'WV',
'Wisconsin'             : 'WI',
'Wyoming State'         : 'WY',
}  


if __name__ == '__main__':
    main()
