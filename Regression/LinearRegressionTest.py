import numpy as np
from random import seed, gauss
import LinearRegression

def getRandomData(mcount):
	seed(1)
	inputs = np.matrix([
		[gauss(0, 1) for i in range(1, mcount + 1)], 
		[gauss(0, 1)  for i in range(1, mcount + 1)]])
	outputs = LinearRegression.addOneRow(inputs).T * np.matrix([[5], [3], [4]]) + gauss(0, 0.1)  # weights = [5, 3, 4]
	return inputs, outputs

a, b = getRandomData(3000)

weights = LinearRegression.teachLinReg(a, b)
#w2 = LinearRegression.batchGradientDescent(linder, a, b, np.matrix([[0, 0, 0]]).T, 0.0005, 4000)
print weights
print LinearRegression.calcLinRegError(a, b, weights)
#print LinearRegression.calcLinRegError(a, b, w2)