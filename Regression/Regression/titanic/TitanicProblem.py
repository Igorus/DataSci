import sys
sys.path.append("../")

import LogisticRegression as lr
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


w, e = lr.batchGradientDescent(inputs, outputs, np.matrix([[0] * 7]).T, 0.5, -0.01, 100)
print e[0:4], '...'
print e[-5:-1]

"""s = 0.0
for m in range(outputs.shape[0]):
	s = s + np.abs(lr.calcLogReg(w, inputs[:, m], 0.5) - outputs[m])

print float(s) / outputs.shape[0]"""




csv_file_objectT = csv.reader(open('test.csv', 'rb')) #Load in the csv file
headerT = csv_file_objectT.next() #Skip the fist line as it is a header

dataT=[] #Creat a variable called 'data'
for row in csv_file_objectT: #Skip through each row in the csv file
    dataT.append(row) #adding each row to the data variable
dataT = np.array(dataT) #Then convert from a list to an array

#print header
#pclass,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked
#pclass0-0,name1,sex2-1,age3-2,sibsp4-3,parch5-4,ticket6,fare7-5,cabin8,embarked9
inputs = dataT[0:, (0, 2, 3, 4, 5, 7)]
inputs[:, 1] = lr.eapply(lambda x: int(x), dataT[0::,2] == "male")
inputs = np.matrix(lr.eapply(liq, inputs))

inputs = np.matrix(inputs).T.astype(float)

testResult = [lr.calcLogReg(w, inputs[:, m], 0.5) for m in range(inputs.shape[1])]

open_file_object = csv.writer(open("../output.csv", "wb"))

for i in xrange(len(dataT[:,0])):
	open_file_object.writerow([testResult[i]] + list(np.array(dataT[i,:]).reshape(-1))) #Write the row to the file