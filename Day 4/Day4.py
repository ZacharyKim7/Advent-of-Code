# with open('Data4.txt') as f:
#     lines = [line.strip() for line in f]

# overlap = 0
# for pair in lines:
#     current = pair.split(",")
#     numbers = []
#     for range in current:
#         numbers.append(range.split("-"))
#     if ((int(numbers[0][0]) <= int(numbers[1][0])) and (int(numbers[0][1]) >= int(numbers[1][1]))):
#         overlap += 1
#     elif ((int(numbers[1][0]) <= int(numbers[0][0])) and (int(numbers[1][1]) >= int(numbers[0][1]))):
#         overlap += 1



# print(overlap)

# Part 2
with open('Data4.txt') as f:
     lines = [line.strip() for line in f]

overlap = 0
for pair in lines:
    current = pair.split(",")
    numbers = []
    for range in current:
        numbers.append(range.split("-"))
    
    if (int(numbers[1][0]) <= int(numbers[0][0]) <= int(numbers[1][1])):
        overlap += 1
    elif (int(numbers[1][0]) <= int(numbers[0][1]) <= int(numbers[1][1])):
        overlap += 1
    elif (int(numbers[0][0]) <= int(numbers[1][0]) <= int(numbers[0][1])):
        overlap += 1
    elif (int(numbers[0][0]) <= int(numbers[1][1]) <= int(numbers[0][1])):
        overlap += 1

print(overlap)