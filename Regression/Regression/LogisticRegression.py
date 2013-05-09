import numpy as np
from math import exp

def addOneRow(matrix):
	return np.concatenate(
		(np.matrix([1] * matrix[0, :].shape[1]), matrix),
		axis=0)


def eapply(function, matrix):
	vecFunction = np.vectorize(function)
	return vecFunction(matrix)


def normalizeData(inputs):
	inp = np.matrix(np.zeros(shape = inputs.shape))
	m = [0] * inp.shape[0]
	s = [0] * inp.shape[0]
	for i in range(inp.shape[0]):
		m[i] = np.mean(inputs[i, :])
		s[i] = np.std(inputs[i, :])
		inp[i, :] = ( (inputs[i, :]) - m[i]) / s[i]
	return inp, m, s


def denormalizeWeights(weightsNorm, m, s):
	newWeights = np.matrix(np.zeros(shape = weightsNorm.shape))
	for i in xrange(1, weightsNorm.shape[0]):
		newWeights[i,0] = weightsNorm[i,0] / s[i - 1]

	newWeights[0,0] = weightsNorm[0,0]
	for j in xrange(1, weightsNorm.shape[0]):
		newWeights[0,0] = newWeights[0,0] - newWeights[j, 0] * m[j - 1]
	return newWeights


# for Logistic Regression alpha < 0, for Linear Regression alpha > 0
def batchGradientDescent(inputs, outputs, weights, threshold, alpha, iterations):
	newWeights = np.matrix(weights)
	inputsNorm, m, s = normalizeData(inputs)

	Error = [calcLogRegError(inputsNorm, outputs, newWeights, threshold)]
	for iteration in xrange(iterations):
		deltaW = LogisticDerivative(inputsNorm, outputs, newWeights)
		newWeights = newWeights - alpha * deltaW
		Error.append(calcLogRegError(inputsNorm, outputs, newWeights, threshold))
		if Error[-1] > Error[-2]: alpha = alpha * 0.99
	return denormalizeWeights(newWeights, m, s), Error


def calcLogReg(weights, inputs, threshold):
	inp = addOneRow(inputs)
	if weights.shape == inp.shape:
		return int(sigmoid(inp.T * weights) > threshold)


def calcLogRegError(inputs, outputs, weights, threshold):
	inp = addOneRow(inputs)
	vecS = np.vectorize(sigmoid)
	hypothesys = np.matrix( vecS(inp.T * weights) )
	result = np.vectorize(int)(np.vectorize(int)(hypothesys > threshold) != outputs)
	
	return np.sum(result) / float(outputs.shape[0])


def sigmoid(x):
	return 1 / (1 + exp(-x))


def LogisticDerivative(inputs, outputs, weights):
	inp = addOneRow(inputs)
	return inp * ( outputs - np.matrix(eapply(sigmoid, inp.T * weights)))

