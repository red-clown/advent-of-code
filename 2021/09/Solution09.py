# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:16:53 2021

@author: XVQH683
"""

example="""2199943210
3987894921
9856789892
8767896789
9899965678"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]

heights=[[int(x) for x in line] for line in lines]
#print ('\n'.join([''.join([str(x) for x in height]) for height in heights]))
for i in (len(heights), 0):
    heights.insert(i, [9 for x in range(len(heights[0]))])
for x in range(len(heights)):
    for i in (len(heights[x]), 0):
        heights[x].insert(i, 9 )

basin_list=[]
for x in range(-1, 2):
    for y in range(-1, 2):
        if abs(x+y) ==1: basin_list.append((x, y))
def basin_exploration(lst, x, y, explored=[]):
    explored.append((x, y))
    size = 1
    for i, j in basin_list:
        if lst[y+i][x+j] > lst[y][x] and lst[y+i][x+j] < 9 and (x+j, y+i) not in explored:
            size+=basin_exploration(lst, x+j, y+i, explored)
    return size

minimums=0
danger=0
basins = []
for y in range(1, len(heights)-1):
    for x in range(1, len(heights[y])-1):
        top = heights[y-1][x]
        bottom =  heights[y+1][x]
        left = heights[y][x-1]
        right = heights[y][x+1]
        if heights[y][x] < min(top, bottom, left, right):
            minimums+=1
            danger+=(1+heights[y][x])
            basins.append(basin_exploration(heights, x, y))
                
            
print('minimums: ', minimums)
print('danger level: ', danger)
print('basins: ', basins)
basin_value = 1
for x in range(3):
    basin_value*=max(basins)
    basins.remove(max(basins))
print('basins value: ', basin_value)