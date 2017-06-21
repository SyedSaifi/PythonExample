'''
Created on Feb 19, 2017

@author: ssaifi
'''
def studentScore(name,score):
    print(name," scored", score," marks.")
    
studentScore("Mark", 90)

def scoreSum(*args):
    sum=0
    for x in args:
        sum = sum+x
    return sum

print(scoreSum(10,20,30))

def marksSum(**args):
    sum=0
    for x in args.values():
        sum = sum+x
    return sum

print(marksSum(maths=100,Hindi=90,SS=80))
