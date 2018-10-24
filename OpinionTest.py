from methods import *

attributeWords = [{'title':'Good','words': [('bad','good')]},
{'title':'Positive','words':['negative','positive']},
{'title':'Useful','words': [('useless','useful')]},
{'title':'Practical','words':['impractical','practical']},
{'title':'Valuable','words':[('worthless','valuable')]},
{'title':'Convenient','words':[('inconvenient','convenient')]},
{'title': 'Simple','words':[('complex','simple')]}]

gender = ['men','women','male','female','boy','girl','masculine','feminine']
ethnicities = ['african','asian','european','american','hispanic','latino']
characteristics = ['openness','conscientiousness','extraversion','agreeableness','neuroticism']

p.pprint(computeScores(gender,attributeWords))
p.pprint(computeScores(ethnicities,attributeWords))
p.pprint(computeScores(characteristics,attributeWords))