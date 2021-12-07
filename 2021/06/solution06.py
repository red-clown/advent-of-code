# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:18:04 2021

@author: Red
"""
example = """3,4,3,1,2"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]


fish =[]
for line in lines:
    tmp= [int(x) for x in line.split(',') ]
    for t in tmp:
        fish.append(t)
print('initial day:', fish)
"""
for day in range(80):
    new_fish=[]
    for i in range(len(fish)):
        if fish[i]==0:
            new_fish.append(8)
            fish[i]=6
        else:
            fish[i]-=1
    for n in new_fish:
        fish.append(n)
    print('day', day+1, ':', len(fish))

print( 'number of fish:', len(fish))
"""

fish_dict={x:0 for x in range(9)}
for f in set(fish):
    fish_dict[f] += fish.count(f)
 
for day in range(256):
    new_fish={x:0 for x in range(9)}
    for f in fish_dict:
        if f == 0:
            new_fish[8] += fish_dict[f]
            new_fish[6] += fish_dict[f]
        else:
            new_fish[f-1] += fish_dict[f]
    fish_dict = new_fish
    print( 'day', day+1, ',number of fish:', sum(fish_dict.values()))