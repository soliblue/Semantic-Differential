import numpy 
import pprint as p
# In this file we import the data and bring it in 
# an easily accessible format
# Importing pre-trained word vector reprasentations
# source: https://nlp.stanford.edu/projects/glove/ 
with open('data/glove.6B.50d.txt', 'r') as file:
     content = file.readlines()
# Initialising the dict which will hold all the words 
# and their corresponding vector reprasentations
vectors = {}
# Adding the words to the dict
for line in content:
	entries = line.split(" ")
	word = entries[0]
	vector = [float(entry) for entry in entries[1:]]
	vectors.update({word:numpy.array(vector)})