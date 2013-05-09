import numpy as np
from math import exp


def addOneRow(matrix):
	return np.concatenate(
		(np.matrix([1] * matrix[0, :].shape[1]), matrix),
		axis=0)

def calcLinReg(weights, inputs):
	inputs = addOneRow(inputs)
	if weights.shape == inputs.shape:
		return (inputs.T * weights)[0, 0]

def LinearDerivative(inputs, outputs, weights):
	inp = addOneRow(inputs)
	return inp * (inp.T * weights - outputs)

def calcLinRegError(inputs, outputs, weights):
	a = addOneRow(inputs).T * weights - outputs
	return (a.T * a)[0, 0]

def teachLinReg(inputs, outputs):
	inputs = addOneRow(inputs)
	if inputs[0, :].shape[::-1] == outputs.shape:  # [::-1] make tulpes reversed
		return np.linalg.inv(inputs * inputs.T) * inputs * outputs