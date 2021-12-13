# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:13:31 2021

@author: XVQH683
"""
example="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
lines = [[int(i) for i in line] for line in example.split('\n')]

with open('input.txt') as f:
    lines = f.readlines()
lines = [[int(i) for i in line.replace('\n', '')] for line in lines]


proxy_table = []
for y in range(-1, 2):
    proxy_table+= [(x, y) for x in range(-1, 2) if (x,y) != (0,0)]

def gridprint(table):
    for y in range(len(table)):
        print(''.join([str(table[y][x]) for x in range(len(table[y]))]) )

def glow(x, y, table, passed):
    glows = 0
    if table[y][x] > 9:
        glows+=1
        passed.append((x, y))
        table[y][x] = 0
        for i, j in proxy_table:
            if 0 <= y+j < len(table) and 0 <= x+i < len(table[y+j]) and (x+i, y+j) not in passed:
                table[y+j][x+i]+=1
                glows += glow(x+i, y+j, table, passed)
    return glows
        
glows, pre_glows, step, synchro = 0, 0, 0, 0
#for step in range(100):
while not synchro:
    step+=1
    glowed = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            lines[y][x]+=1 if (x, y) not in glowed else 0
            glows += glow(x, y , lines, glowed)
    print('after step', step+1, ': ', glows, ' glows')
    if glows == pre_glows + 100:
        synchro = step
    pre_glows=glows
    #gridprint(lines)

print(synchro)