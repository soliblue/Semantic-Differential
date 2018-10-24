from methods import *

testOne = [{'title': 'Evaluation','words': [('bad','good')]},
{'title': 'Potency', 'words': [('weak','strong')]},
{'title': 'Activity', 'words': [('passive','active')]}]
testOneAlt = [{'title': 'Evaluation','words': [('bad','good'),('negative','positive')]},
{'title': 'Potency', 'words': [('weak','strong'),('incompetent','competent'),('fragile','tough'),('ineffective','effective')]},
{'title': 'Activity', 'words': [('passive','active'),('indifferent','caring'),('lazy','energetic')]}]

testTwo = [{'title':'Typicality','words':[('rare','regular'),('exclusive','typical')]},
{'title':'Reality','words':[('imaginary','real'),('abstract','concrete')]},
{'title':'Complexity','words':[('simple','complex'),('limited','unlimited'),('usual','mysterious')]},
{'title':'Organisation','words':[('spasmodic','regular'),('changeable','constant'),('disorganized','organized'),('indefinite','precise')]},
{'title':'Stimulation','words':[('boring','interesting'),('trivial','new')]}]

# The original version returns more accurate results
# hypothesis: Using more synonym words lead to better results
testThree = [{'title':'Male','words':[('female','male'),('girl','boy'),('feminine','masculine')]}]
testThreeAlt = [{'title':'Male','words':[('female','male')]}]

testFour = [{'title':'Good','words': [('bad','good')]},
{'title':'Positive','words':['negative','positive']},
{'title':'Useful','words': [('useless','useful')]},
{'title':'Practical','words':['impractical','practical']},
{'title':'Valuable','words':[('worthless','valuable')]},
{'title':'Convenient','words':[('inconvenient','convenient')]},
{'title': 'Simple','words':[('complex','simple')]}]
testFourAlt = [{'title':'Good/Positive','words':[('bad','good'),('negative','positive')]},
{'title':'Useful/Valuable/Practical','words':[('useless','useful'),('worthless','valuable'),('impractical','practical')]},
{'title':'Easy/Simple','words':[('hard','easy'),('complex','simple')]}]

testFive = [{'title':'Hardworking','words':[('lazy','hardworking')]},{'title':'Beautiful','words':[('ugly','beautiful')]}]

# This is the Word-Embedding Association Test
testSix = [{'title':'Pleasant','words':[('unpleasant','pleasant')]},
{'title':'Male','words':[('female','male')]},
{'title':'Temporary','words':[('permanent','temporary')]},
{'title':'Career','words':[('family','career')]}]


p.pprint(computeScores(['man','woman'],testOne))
p.pprint(computeScores(['man','woman'],testOneAlt))
p.pprint(computeScores(['man','woman'],testTwo))
p.pprint(computeScores(['man','woman'],testThree))
p.pprint(computeScores(['man','woman'],testThreeAlt))
p.pprint(computeScores(['man','woman'],testFive))


p.pprint(computeScores(['openness','closeness'],testFour))
p.pprint(computeScores(['organisation','chaos'],testFour))
p.pprint(computeScores(['extraversion','introversion'],testFour))
p.pprint(computeScores(['extraversion','introversion'],testFourAlt))
p.pprint(computeScores(['openness','conscientiousness','extraversion','agreeableness','neuroticism'],testFour))
p.pprint(computeScores(['openness','conscientiousness','extraversion','agreeableness','neuroticism'],testFourAlt))
p.pprint(computeScores(['asian','african','european'],testFour))
p.pprint(computeScores(['asian','african','european'],testOneAlt))
p.pprint(computeScores(['asian','african','european'],testFive))
p.pprint(computeScores(['insects','flowers'],testSix))
p.pprint(computeScores(['man','woman'],testSix))
