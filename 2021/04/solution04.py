# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:39:34 2021

@author: Red
"""
example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n', '') for x in lines]

drawing = [int(x) for x in lines[0].split(',')]
print(drawing)

boards=[]
board_index=0
boards.append([])
for line in lines[2::]:
    if line == '':
        board_index+=1
        boards.append([])
    else:
        temp_line={int(line[(3*x):min((3*x+3), len(line))]):False 
                   for x in range(round(len(line)/3+.5))}      
        boards[board_index].append(temp_line)

print(boards)

winner =[]
for x in drawing:
    print('draw: ',x)
    for board in boards:
        if winner: break
        column_index = []
        for line in board:
            if winner: break
            if x in line:
                line[x] = True
                column_index.append(list(line.keys()).index(x))
                if False not in line.values():
                    winner = board
                    print ('line_winner: ', line)
                    print ('temp_winner: ', winner)
                    break
        for c in column_index:
            column={}
            for line in board:
                temp_key = list(line.keys())[c]
                column[temp_key]=line[temp_key]
            if False not in column.values():
                winner = board
                print ('column_winner: ', line)
                print ('temp_winner: ', winner)
    final_draw = x
    if winner: break
            
print ('winner: ', winner)
winner_sum = 0
for line in winner:
    for x in line:
        winner_sum+= x if line[x]==False else 0


print ('winner final score: ', winner_sum * final_draw)

winner=[]
for board in boards:
    for line in board:
        for x in line:
            line[x]=False
print(boards)
for x in drawing:
    print('draw: ',x)
    winner=[]
    for board in boards:
        column_index = []
        for line in board:
            if x in line:
                line[x] = True
                column_index.append(list(line.keys()).index(x))
                if False not in line.values() and board not in winner:
                    winner.append(board)
                    print ('line_winner: ', line)
        for c in column_index:
            column={}
            for line in board:
                temp_key = list(line.keys())[c]
                column[temp_key]=line[temp_key]
            if False not in column.values() and board not in winner:
                winner.append(board)
                print ('column_winner: ', column)
    final_draw = x
    if winner:
        for b in winner:
            boards.remove(b)
    if not boards: 
        break

print ('last winner: ', winner)
winner_sum = 0
for line in winner[0]:
    for x in line:
        winner_sum+= x if line[x]==False else 0

print ('last winner final score: ', winner_sum * final_draw)