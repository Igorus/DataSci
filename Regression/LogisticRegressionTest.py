import numpy as np
from random import seed, gauss
import LogisticRegression as lr

i = np.matrix([
	[1,1], [1,2], [1,3],
	[2,1], [2,2], [2,3],
	[3,1], [3,2], [3,3]
	]).T

o = np.matrix([[0, 0, 1, 0, 1, 1, 1, 1, 1]]).T

w = lr.batchGradientDescent(
	lr.LogisticDerivative, 
	i, o, np.matrix([[0], [0], [0]]), -0.5, 70)

print w

for i in xrange(3):
	for v in xrange(3):
		print i, v, lr.calcLogReg(w, np.matrix([i+1,v+1]).T, 0.5)

print lr.calcLogReg(w, np.matrix([3,0.85352157]).T, 0.5)