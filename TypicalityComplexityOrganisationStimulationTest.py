from methods import *

attributeWords = [{'title':'Typicality','words':[('rare','regular'),('exclusive','typical')]},
{'title':'Reality','words':[('imaginary','real'),('abstract','concrete')]},
{'title':'Complexity','words':[('simple','complex'),('limited','unlimited'),('usual','mysterious')]},
{'title':'Organisation','words':[('spasmodic','regular'),('changeable','constant'),('disorganized','organized'),('indefinite','precise')]},
{'title':'Stimulation','words':[('boring','interesting'),('trivial','new')]}]

gender = ['men','women','male','female','boy','girl','masculine','feminine']
ethnicities = ['african','asian','european','american','hispanic','latino']
characteristics = ['openness','conscientiousness','extraversion','agreeableness','neuroticism']

p.pprint(computeScores(gender,attributeWords))
p.pprint(computeScores(ethnicities,attributeWords))
p.pprint(computeScores(characteristics,attributeWords))