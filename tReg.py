import numpy as np
from random import seed, gauss
import Regressions
from Regressions import addOneRow as addOneRow

""" test for log reg
i = np.matrix([
	[1,1], [1,2], [1,3],
	[2,1], [2,2], [2,3],
	[3,1], [3,2], [3,3]
	]).T
o = np.matrix([[0, 0, 1, 0, 1, 1, 1, 1, 1]]).T
w = batchGradientDescent(LogisticDerivative, i, o, np.matrix([[0], [0], [0]]), -0.5, 70)
print w

for i in xrange(3):
	for v in xrange(3):
		print i, v, calcLogReg(w, np.matrix([i+1,v+1]).T, 0.5)

print calcLogReg(w, np.matrix([3,0.85352157]).T, 0.5)
"""


#test for lin reg
def getRandomData(mcount):
	seed(1)
	inputs = np.matrix([
		[gauss(0, 1) for i in range(1, mcount + 1)], 
		[gauss(0, 1)  for i in range(1, mcount + 1)]])
	outputs = addOneRow(inputs).T * np.matrix([[5], [3], [4]]) + gauss(0, 0.1)  # weights = [5, 3, 4]
	return inputs, outputs

a, b = getRandomData(3000)

weights = Regressions.teachLinReg(a, b)
w2 = Regressions.batchGradientDescent(linder, a, b, np.matrix([[0, 0, 0]]).T, 0.0005, 4000)
print weights
print w2
print Regressions.calcLinRegError(a, b, weights)
print Regressions.calcLinRegError(a, b, w2)
#print calcLinReg(weights, np.matrix([[2], [3]]))