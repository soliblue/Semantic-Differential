from methods import *

attributeWords = [{'title':'Pleasant','words':[('unpleasant','pleasant')]},
{'title':'Male','words':[('female','male')]},
{'title':'Temporary','words':[('permanent','temporary')]},
{'title':'Career','words':[('family','career')]}]

gender = ['men','women','male','female','boy','girl','masculine','feminine']
ethnicities = ['african','asian','european','american','hispanic','latino']
characteristics = ['openness','conscientiousness','extraversion','agreeableness','neuroticism']

# Specifically, they demonstrated that flowers are significantly more pleasant than insects, 
# based on the reaction latencies of four pairings (flowers + pleasant, insects + unpleasant, 
# flowers + unpleasant, and insects + pleasant).  
# Similarly, we replicated Greenwald et al.s finding (5) that musical instruments are 
# significantly more pleasant than weapons (see Table 1).
# mathematics more male
# arts more female
# science in general is associated more with female
test = ['insects','flowers','music','war','life','death','mathematics','arts','science']
# This yields the expected answers exactly

p.pprint(computeScores(gender,attributeWords))
p.pprint(computeScores(ethnicities,attributeWords))
p.pprint(computeScores(characteristics,attributeWords))
p.pprint(computeScores(test,attributeWords))