with open('Day2/data2.txt') as f:
    lines = [line.strip() for line in f]

def part_one(lines):
    answer = 0
    for line in lines:
        report = line.split(" ")
        answer += 1 if isValid(report) else 0
    
    return answer

def part_two(lines):
    answer = 0
    for line in lines:
        report = line.split(" ")
        answer += 1 if isValid2(report) else 0
    
    return answer

def isValid(report):
    increasing = True
    for i in range(1, len(report)):
        if not (1 <= int(report[i]) - int(report[i - 1]) <= 3):
            increasing = False


    decreasing = True
    for i in range(1, len(report)):
        if not (-3 <= int(report[i]) - int(report[i - 1]) <= -1):
            decreasing = False


    return increasing or decreasing

def isValid2(report):
    if isValid(report):
        return True

    for i in range(len(report)):
        modified_report = report[: i] + report[i + 1:]
        if isValid(modified_report):
            return True

    return False


print(part_one(lines))
print(part_two(lines))
