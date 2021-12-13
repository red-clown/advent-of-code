# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:16:17 2021

@author: XVQH683
"""

example="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
lines = example.split('\n')


with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]


errors, incompletes= [], []
transdict = {'(': ')', '[': ']', '<': '>', '{': '}'}
errorscore = {')': 3, ']': 57, '}':1197, '>': 25137}
compscore = {')': 1, ']': 2, '}': 3, '>': 4}
for line in lines:
    error = ''
    stack = []
    for x in line:
        if x in transdict:
            stack.append(transdict[x])
        else:
            test = stack.pop() if len(stack)>0 else ''
            error = x if x != test else ''
        if error:
            break
    if error:
        errors.append(error)
    else:
        stack.reverse()
        score = 0
        for x in stack:
            score = 5*score + compscore[x]
        incompletes.append(score)

score1 = sum([errorscore[x] for x in errors])

print ('error score: ', score1)
def median(a):
    sortedLst = sorted(a)
    lstLen = len(a)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
print ('complete score: ', median(incompletes))