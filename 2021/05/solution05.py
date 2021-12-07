# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:47:48 2021

@author: Red
"""
example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]

vecteurs=[]
x_display, y_display = (0, 0)
for line in lines:
    départ, arrivée = line.split(' -> ', 2)
    x1, y1 = map(int, départ.split(',', 2))
    x2, y2 = map(int, arrivée.split(',', 2))
    vecteurs.append(((x1, y1), (x2, y2)))
    x_display = max(x_display, x1, x2)
    y_display = max(y_display, y1, y2)

print(x_display, y_display)
def gridprint(d):
    for y in range(y_display+1):
        line = []
        for x in range(x_display+1):
            if (x, y) in d:
                line.append(str(d[x, y]))
            else:
                line.append('.')
        print(' '.join(line))

grille={}
for vecteur in vecteurs:
    if vecteur[0][0] == vecteur[1][0]:
        x = vecteur[0][0]
        y1 = min(vecteur[0][1], vecteur[1][1])
        y2 = max(vecteur[0][1], vecteur[1][1])+1
        for y in range(y1, y2):
            if (x, y) in grille:
                grille[(x, y)]+=1
            else:
                grille[(x, y)]=1
    elif vecteur[0][1] == vecteur[1][1]:
        y = vecteur[0][1]
        x1 = min(vecteur[0][0], vecteur[1][0])
        x2 = max(vecteur[0][0], vecteur[1][0])+1
        for x in range(x1,x2):
            if (x, y) in grille:
                grille[(x, y)]+=1
            else:
                grille[(x, y)]=1
    elif abs(vecteur[0][0] - vecteur[1][0]) == abs(vecteur[1][1] - vecteur[0][1]):
        stp = vecteur[1][0] - vecteur[0][0]
        sensx = stp//abs(stp)
        sensy = (vecteur[1][1] - vecteur[0][1])//abs(vecteur[1][1] - vecteur[0][1])
        x = vecteur[0][0]        
        y = vecteur[0][1]
        for i in range(abs(stp)+1):
            if (x + i*sensx, y + i*sensy) in grille:
                grille[(x + i*sensx, y + i*sensy)]+=1
            else:
                grille[(x + i*sensx, y + i*sensy)]=1

    

    

gridprint(grille)
dangers=0
for point in grille.values():
    if point > 1:
        dangers+=1

print(dangers)