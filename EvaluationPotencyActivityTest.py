from methods import *

attributeWords = [{'title': 'Evaluation (Good)','words': [('bad','good')]},
{'title': 'Potency (Strong)', 'words': [('weak','strong')]},
{'title': 'Activity (Active)', 'words': [('passive','active')]}]

gender = ['men','women','male','female','boy','girl','masculine','feminine']
ethnicities = ['african','asian','european','american','hispanic','latino']
characteristics = ['openness','conscientiousness','extraversion','agreeableness','neuroticism']

p.pprint(computeScores(gender,attributeWords))
p.pprint(computeScores(ethnicities,attributeWords))
p.pprint(computeScores(characteristics,attributeWords))