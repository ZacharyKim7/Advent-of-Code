with open('Day1/data1.txt') as f:
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
    for i in range(len(lines)):
        if lines[i][:5] not in count:
            count[lines[i][:5]] = 1

        if lines[i][:8] in count:
            count[lines[i][:5]] += 1

    for key, value in count.items():
        answer += int(key) * int(value)
    
    return answer

print(part_two(lines))
