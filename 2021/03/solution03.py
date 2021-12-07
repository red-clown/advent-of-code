# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:23:27 2021

@author: Red
"""

example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()

def mean(a):
    return sum(a)/len(a)

print(lines[0])
print(len(lines[0]))
gammas=[]
for x in range(len(lines[0])-1):
    temp =round(mean([int(y[x]) for y in lines]))
    gammas.append(temp)
    
epsilons=[str((temp-1)**2) for temp in gammas]
gamma=int(''.join(map(str, gammas)), 2)
epsilon=int(''.join(epsilons), 2)

print('gamma = ',gamma)
print('epsilon = ',epsilon)
print('power = ',gamma*epsilon)

oxy_list = [x for x in lines]
co2_list= [x for x in lines]
oxygens=[]
co2s=[]
def clean_list(l, x, a):
    remove_list=[]
    for y in l:
        if y[x] != a:
            remove_list.append(y)
    for z in remove_list:
        l.remove(z)
for x in range(12):
    oxy_temp =int(mean([int(y[x]) for y in oxy_list])+0.5)
    clean_list(oxy_list, x, str(oxy_temp))
    oxygens.append(oxy_temp)
    if len(oxy_list) == 1:
        oxygens=list(oxy_list[0])
        break
for x in range(12):
    co2_temp =(int(mean([int(y[x]) for y in co2_list])+.5)-1)**2
    clean_list(co2_list, x, str(co2_temp))
    co2s.append(co2_temp)   
    if len(co2_list) == 1:
        co2s=list(co2_list[0])
        break

oxygen=int(''.join(map(str, oxygens)), 2)
co2=int(''.join(map(str, co2s)), 2)
print('oxygen= ', oxygen)
print('co2= ', co2)
print('life_support= ', oxygen * co2)

  
#    co2_temp =(round(mean([int(y[x]) for y in co2_list]))-1)**2
    
    