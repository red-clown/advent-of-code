import re

def process_input(schematics:list[str]):
    x=0
    numbers={}
    symbols=set()
    symbol_pattern = re.compile(r'[^0-9.\r\n]')
    number_pattern = re.compile(r'[0-9]')
    for line in schematics:
        print(line)
        m=len(line)+1
        y=0
        for symbol_match in symbol_pattern.finditer(line):
            y = symbol_match.span()[0]
            for i in range(3):
                for j in range(3):
                    x1=x+i-1
                    y1=y+j-1
                    if x1>=0 and y1>=0 and x1<m and y1<m: symbols.add((x1,y1))
        for number_match in number_pattern.finditer(line):
            c = number_match.group()
            numbers[c]=list()
            s1, s2 =number_match.span()
            for y in range(s1, s2):
                (numbers[c]).append[(x,y)]
        x+=1
        print(numbers)
    


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as input_values:
        schematics = input_values.readlines()[0:10]

    process_input(schematics)

    #part_1_ans = part_1(raw_calibration)
    #print("part 1 answer:", part_1_ans)

    #part_2_ans = part_2(raw_calibration)
    #print("part 2 answer:", part_2_ans)