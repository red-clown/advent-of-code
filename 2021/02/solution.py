# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:53:12 2021

@author: Red
"""
with open('input.txt') as f:
    lines = f.readlines()
    
#lines=('forward 5','down 5','forward 8','up 3','down 8','forward 2')

x, y, a=(0, 0, 0)
for txt in lines:
    t2=txt.split()
    if t2[0]=='forward':
        x+=int(t2[1])
        y+=int(t2[1])*a
    elif t2[0]=='down':
        a+=int(t2[1])
    elif t2[0]=='up':
        a-=int(t2[1])
        
print(x, '*', y, '=', x*y )