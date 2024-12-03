with open(r"Advent-of-Code\2024\Day1\data1.txt") as f:
    lines = [line.strip() for line in f]

def part_one(lines):
    leftVals = []
    rightVals = []

    for line in lines:
        leftVals.append(int(line[:5]))
        rightVals.append(int(line[8:]))

    leftVals.sort()
    rightVals.sort()

    answer = 0
    for i in range(len(leftVals)):
        answer += abs(leftVals[i] - rightVals[i])

    return answer

def part_two(lines):
    answer = 0
    countRight = {} 
    for line in lines:
        if line[8:] not in countRight:
            countRight[line[8:]] = 1
        else:
            countRight[line[8:]] += 1
    
    for i in range(len(lines)):
        if lines[i][:5] in countRight:
            answer += int(lines[i][:5]) * countRight[lines[i][:5]]
    
    return answer

print(part_one(lines))
print(part_two(lines))
