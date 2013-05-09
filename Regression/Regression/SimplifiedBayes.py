import numpy as np

def teachBayes(inputs, outputs):
	featureCount = inputs.shape[0]
	inputCount = inputs.shape[1]

	probabilities = []
	counts = []

	for i in range(featureCount):
		probabilities.append({})
		counts.append({})
		for j in range(inputCount):
			if inputs[i,j] not in probabilities[i]:
				probabilities[i][inputs[i,j]] = 0
				counts[i][inputs[i,j]] = 0

			if outputs[j] == 1:
				probabilities[i][inputs[i,j]] = probabilities[i][inputs[i,j]] + 1
			
			counts[i][inputs[i,j]] = counts[i][inputs[i,j]] + 1

		for k in probabilities[i].keys():
			probabilities[i][k] = float(probabilities[i][k]) / counts[i][k]
	return probabilities

def calcBayes(inputs, probDict):
	pr = 0.5
	npr = 0.5
	for i in range(inputs.shape[0]):
		if inputs[i, 0] in probDict[i]:
			pr = pr * probDict[i][inputs[i, 0]]
			npr = npr * (1 - probDict[i][inputs[i, 0]])
	print pr, npr
	return int(pr > npr)