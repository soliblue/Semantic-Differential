from processData import *

def dist(x,y):   
	return numpy.sqrt(numpy.sum((x-y)**2))

def cosSim(x,y):   
	return numpy.sum((x*y)) / (numpy.sqrt(numpy.sum(x**2)) * numpy.sqrt(numpy.sum(y**2)))

def computeScores(words,testData):
	result = {}
	for word in words:
		result.update({word:[]})
		for data in testData:
			tempResult = 0
			for wordPair in data['words']:
				firstWord = wordPair[0]
				secondWord = wordPair[1]
				firstWordDistance = dist(vectors[firstWord],vectors[word])
				secondWordDistance = dist(vectors[secondWord],vectors[word])
				tempResult += firstWordDistance / secondWordDistance
			result[word].append({data['title']:tempResult / len(data['words'])})
	return result