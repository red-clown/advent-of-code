from collections import namedtuple
import re

Game=namedtuple('Game',['red','green','blue'])

def process_input(game_result:list[str]) -> list[(int, list[Game])]:
    proc_result =[]
    for line in game_result:
        part_ID, part_dice= line.split(':')
        ID=int(part_ID.split(' ')[1])
        sets=[]
        for set in part_dice.split(';'):
            r = re.search(r'\d+(?= red)', set)
            red = int(r.group()) if r else 0
            g =re.search(r'\d+(?= green)', set)
            green=int(g.group()) if g else 0
            b = re.search(r'\d+(?= blue)', set)
            blue=int(b.group()) if b else 0
            sets.append(Game(red, green, blue))
        proc_result.append((ID,sets))
    
    return proc_result
            
def part_1(game_data:list[(int, list[Game])], max_game:Game)-> int:
    aggregate = 0
    for game in game_data:
        ok_set = True
        for set in game[1]:
            if set.red > max_game.red or\
               set.green > max_game.green or\
               set.blue > max_game.blue:
                ok_set = False
            quit
        if ok_set:
            aggregate+=game[0]
    return aggregate

def part_2(game_data:list[(int, list[Game])])-> int:
    aggregate=0
    for game in game_data:
        min_game=Game(0,0,0)
        for set in game[1]:
            min_game=Game(max(set.red,min_game.red),max(set.green,min_game.green),max(set.blue,min_game.blue))
        aggregate += min_game.red*min_game.green*min_game.blue
    return aggregate


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as input_values:
        raw_result = input_values.readlines()

    proc_result = process_input(raw_result)
    
    part_1_ans = part_1(proc_result,Game(red=12, green=13, blue=14))
    print("part 1 answer:", part_1_ans)

    part_2_ans = part_2(proc_result)
    print("part 2 answer:", part_2_ans)