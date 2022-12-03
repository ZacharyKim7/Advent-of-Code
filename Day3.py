# with open('Data3.txt') as f:
#     lines = [line.strip() for line in f]

# common = []
# for string in lines:
#     half1 = string[0:int(len(string) / 2)]
#     half2 = string[int(len(string) / 2):int(len(string))]
#     both = set(half1).intersection(set(half2))
#     common.append("".join(both))

# values = {}
# value = 1
# for i in range(97, 123):
#     values[chr(i)] = value
#     value += 1

# value = 27
# for i in range(65, 91):
#     values[chr(i)] = value
#     value += 1

# score = 0
# for character in common:
#     score += int(values[character])

# print(score)

# Part 2
with open('Data3.txt') as f:
    lines = [line.strip() for line in f]

common = []
position = 0
for i in range(int(len(lines) / 3)):
    current = []
    for j in range(3):
        current.append(lines[position])
        position += 1
    elf1, elf2, elf3 = set(current[0]), set(current[1]), set(current[2])
    all_three = set(elf1) & set(elf2) & set(elf3)
    common.append("".join(all_three))

values = {}
value = 1
for i in range(97, 123):
    values[chr(i)] = value
    value += 1

value = 27
for i in range(65, 91):
    values[chr(i)] = value
    value += 1

score = 0
for character in common:
    score += int(values[character])

print(score)



