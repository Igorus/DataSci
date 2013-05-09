import sys
sys.path.append("../")

import LogisticRegression as lr
import SimplifiedBayes as sb
import csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the fist line as it is a header
data=[] #Creat a variable called 'data'
for row in csv_file_object: #Skip through each row in the csv file
    data.append(row) #adding each row to the data variable
data = np.array(data) #Then convert from a list to an array

#print header

#survived0,pclass1-0,name2,sex3-1,age4-2,sibsp5-3,parch6-4,ticket7,fare8-5,cabin9,embarked10
outputs = np.matrix(data[0:, 0]).T.astype(int)
inputs = data[0:, (1, 3, 4, 5, 6, 8)]
inputs[:, 1] = lr.eapply(lambda x: int(x), data[0::,3] == "male")

def liq(x): 
	if x == '': return 0
	else: return x
inputs = np.matrix(lr.eapply(liq, inputs))
inputs = np.matrix(inputs).T.astype(float)

def clasterize(vector, classCount):
	a = list(np.array(vector).reshape(-1))
	maxv, minv = max(a), min(a)
	h = float(maxv - minv) / classCount
	return [ int((x - minv) / h)  for x in a]

classCount = 4
clasterized = (2, 3, 5)
for i in clasterized:
	inputs[i,:] = clasterize(inputs[i,:], classCount)

print inputs
pr = sb.teachBayes(inputs, outputs)
for i in pr: print i

print sb.calcBayes(np.matrix([[1, 0, 2, 0, 1, 1]]).T, pr)