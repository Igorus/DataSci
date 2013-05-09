import numpy as np
import random

def calcLinReg(weights, inputs):
	if len(weights) == len(inputs) + 1:
		inputs = np.matrix([1] + inputs)
		weights = np.matrix(weights)
		return (weights * np.transpose(inputs))[0,0]
	return None

def teachLinReg(inputs, outputs):
	if len(inputs[0]) == len(outputs):
		i = [1 for i in range(1, len(inputs[0]))]
		print len(i), len(inputs[0])
		a = np.matrix(i + inputs)
		print a
		b = []
		return np.linalg.solve(a, b)


random.seed(1)
a = [[random.gauss(0, 1) for i in range(1,10)], [random.gauss(5, 1.5)  for i in range(1,10)]]
b = []
print b
for i in range(0, len(a[0])):
	b.insert(i, 3 * a[0][i] + 4 * a[1][i] + 5 + random.gauss(0, 0.1))
	print a[0][i], a[1][i], b[i]

teachLinReg(a, b)
print calcLinReg([1,2,3], [2, 4])


#print n.matrix([[1,2,3],[4,5,6]])