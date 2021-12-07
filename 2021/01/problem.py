# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:49:37 2021

@author: Red
"""
with open('input.txt') as f:
    lines = f.readlines()

#excercise 1: increases
depths= []
increase_counter=0

depths.append((int(lines[0]), '0'))
for line in lines[1::]:
    depth= int(line)
    dif = '0'
    if depth > depths[-1][0]:
        dif = '+'
        increase_counter+=1
    depths.append((depth, dif))
   
print('increases: ', increase_counter)

#execercise 2 - three-value increases
#lines = (199, 200,208,210,200,207,240,269,260,263)

tsum={}
sums=[]
for y in range(3):
    tsum[y]=0
for x in range(len(lines)):
    for y in range(3):
        if x >= y:
            if y==(x%3) and x>=3:
                sums.append(tsum[y])
                tsum[y]=0
            tsum[y]+=int(lines[x])
sums.append(tsum[len(lines)%3])

increase3=0
prev = sums[0]
for z in sums[1::]:
    increase3+=1 if prev < z else 0
    prev = z

print(sums)
print(tsum)
print ('three-measurement increases: ', increase3)