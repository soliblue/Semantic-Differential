from methods import *

attributeWords = [{'title':'Like','words':[('dislike','like')]},{'title':'Positive','words':[('negative','positive')]}]

basicInterests = ['business','finance','teaching','writing','art','science','law','management','mathematics','healthcare','trading','politics','religion','technical']
personalStyles = ['learning','working','leadership','risk','team']
personalStylesAlt = ['learn','work','lead','risk']

p.pprint(computeScores(basicInterests,attributeWords))
p.pprint(computeScores(personalStyles,attributeWords))
p.pprint(computeScores(personalStylesAlt,attributeWords))