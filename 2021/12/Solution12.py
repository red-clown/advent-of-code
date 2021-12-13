# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:38:46 2021

@author: XVQH683
"""

example="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
lines = example.split('\n')

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]

links= {}
for link in lines:
    a, b = link.split('-', 2)
    if a in links:
        if b not in links[a]:
            links[a].append(b)
    else:
        links[a]=[b]
    if b in links:
        if a not in links[b]:
            links[b].append(a)
    else:
        links[b]=[a]
print(links)

def explore(start, end, links, explored=[]):
    paths=[]
    if start == start.upper() or start not in explored:
        explored.append(start)
        if start == end:
            paths.append(explored)
        else:
            for cave in links[start]:
                paths+=explore(cave, end, links, explored[::])
    return paths
    
print(len(explore('start', 'end', links)))