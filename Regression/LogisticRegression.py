import numpy as np
from math import exp


def addOneRow(matrix):
	return np.concatenate(
		(np.matrix([1] * matrix[0, :].shape[1]), matrix),
		axis=0)


def eapply(function, matrix):
	vecFunction = np.vectorize(function)
	return vecFunction(matrix)


# for Logistic Regression alpha < 0, for Linear Regression alpha > 0
def batchGradientDescent(derivativeFunc, inputs, outputs, weights, alpha, iterations):
	newWeights = weights
	for iteration in xrange(iterations):
		deltaW = derivativeFunc(inputs, outputs, newWeights)
		newWeights = newWeights - alpha * deltaW
		#if iteration % 10000 == 0 : print calcLinRegError(inputs, outputs, newWeights)
	return newWeights


def calcLogReg(weights, inputs, threshold):
	inputs = addOneRow(inputs)
	if weights.shape == inputs.shape:
		return int(sigmoid(inputs.T * weights) > threshold)


def sigmoid(x):
	return 1 / (1 + exp(-x))


def LogisticDerivative(inputs, outputs, weights):
	inp = addOneRow(inputs)
	return inp * ( outputs - eapply(sigmoid, inp.T * weights))

