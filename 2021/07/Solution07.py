# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:52:49 2021

@author: Red
"""
import statistics

example = """16,1,2,0,4,2,7,1,2,14"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]


crabs =[]
for line in lines:
    tmp= [int(x) for x in line.split(',') ]
    for t in tmp:
        crabs.append(t)
        
def mean(a):
    return sum(a)/len(a)

def median(a):
    sortedLst = sorted(a)
    lstLen = len(a)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
    

target1=median(crabs)
fuel1 = 0
for pos in crabs:
    fuel1+=abs(pos - target1)

print('fuel 1:', fuel1)

target2=int(mean(crabs))
print(target2)
fuel2 = 0
for pos in crabs:
    fuel2+=abs(pos - target2)*(abs(pos - target2) + 1)/2
print('fuel 2:', fuel2)