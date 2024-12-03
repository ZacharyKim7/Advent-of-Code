with open(r"Advent-of-Code\2024\Day3\data3.txt") as f:
    lines = [line.strip() for line in f]

import re

def part_one(lines):
    answer = 0
    for line in lines:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for match in matches:
            answer += eval(re.findall(r"\d{1,3},\d{1,3}", match)[0].replace(",","*"))
    
    return answer

def part_two(lines):
    answer = 0
    calculate = True
    for line in lines:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for match in matches:
            if match == "do()":
                calculate = True
            elif match == "don't()":
                calculate = False
            else:
                if calculate:
                    answer += eval(re.findall(r"\d{1,3},\d{1,3}", match)[0].replace(",","*"))

    return answer

print(part_one(lines))
print(part_two(lines))
