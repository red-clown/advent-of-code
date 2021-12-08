# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:33:09 2021

@author: Red
"""


example="""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]

training, test =([], [])
for line in lines:
    a, b = [x.split(' ') for x in line.split(' | ') ]
    training.append(a)
    test.append(b)

#print(training)
#part 1
"""
easydigits=0
for display in test:
    for digit in display:
        if len(digit) in (2, 3, 4, 7):
            easydigits+=1

print(easydigits)
"""
#part 2
trained_list=[]
for display in training:
    digits={}
    trained={}
    for digit in display:
        if len(digit) in digits:
            digits[len(digit)].append(sorted(digit))
        else:
            digits[len(digit)]=[sorted(digit)]
    trained[''.join(digits[2][0])]='1'
    trained[''.join(digits[3][0])]='7'
    trained[''.join(digits[4][0])]='4'
    trained[''.join(digits[7][0])]='8'
    right = set(digits[2][0])
    weird_center = set(digits[4][0])-right
    for digit in digits[6]:
        if right - set(digit):
            trained[''.join(digit)]='6'
        elif weird_center - set(digit):
            trained[''.join(digit)]='0'
        else:
            trained[''.join(digit)]='9'
    for digit in digits[5]:
        if not right - set(digit):
            trained[''.join(digit)]='3'
        elif weird_center - set(digit):
            trained[''.join(digit)]='2'
        else:
            trained[''.join(digit)]='5'
    trained_list.append(trained)

print(trained_list)
score=0
for x in range(len(test)):
    output=[]
    for digit in test[x]:
        output.append(trained_list[x][''.join(sorted(digit))])
    score+=int(''.join(output))
print(score)