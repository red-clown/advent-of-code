import re

def part_1(raw_calibration: list[str]) -> int:
    """calibration interperter"""
    digit=['0','1','2','3','4','5','6','7','8','9']
    calibrated = []
    for string in raw_calibration:
        first_digit, last_digit = ' ', ' '
        for i in string:
            if i in digit:
                last_digit=i
                if first_digit==' ': first_digit=i 
        calibrated.append(int(first_digit+last_digit))
        
    return sum(calibrated)

def part_2(raw_calibration: list[str]) -> int:
    """calibration interpreter with written digits"""
    digit={'1':1,
           '2':2,'3':3,
           '4':4,'5':5,
           '6':6,'7':7,
           '8':8,'9':9,
           'one':1, 'two':2, 
           'three':3, 'four':4, 
           'five':5, 'six':6, 
           'seven':7, 'eight':8, 
           'nine':9}
    pattern='(?=('+'|'.join(digit.keys())+'))'
    print(pattern)
    calibrated=0
    for string in raw_calibration:
        print("raw calibration:", string)
        calibration_bits= re.findall(pattern, string)
        first_digit = digit[calibration_bits[0]]*10
        last_digit = digit[calibration_bits[-1]]
        print("regexp:", calibration_bits, first_digit+last_digit)
        calibrated+=first_digit+last_digit
    
    return calibrated

if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as input_values:
        raw_calibration = input_values.readlines()


    part_1_ans = part_1(raw_calibration)
    print("part 1 answer:", part_1_ans)

    part_2_ans = part_2(raw_calibration)
    print("part 2 answer:", part_2_ans)