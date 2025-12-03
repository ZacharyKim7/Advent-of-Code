# from functools import cache

with open("AdventOfCode23\Day 4\Data4.txt") as f:
    lines = [line.strip() for line in f]


# total = 0
# for line in lines:
#     points = 0
#     winning = set(int(num) for num in line[10:39].split())
#     numbers = set(int(num) for num in line[42:116].split())
#     match = numbers.intersection(winning)
#     if len(match) == 0:
#         continue
#     for i in range(len(match)):
#         if i == 0:
#             points = 1
#         else:
#             points *= 2
#     total += points
# print(total)

# @cache
def find_cards(start, matches):
    cards = 0
    for i in range(start + 1, start + matches + 1):
        cards += 1
        winning = set(int(num) for num in lines[i][10:39].split())
        numbers = set(int(num) for num in lines[i][42:116].split())
        match = len(numbers.intersection(winning))
        if match == 0:
            continue 
        else:
            cards += find_cards(i, match)
    return cards

total_cards = 0   
for i in range(len(lines)):
    print(i)
    winning = set(int(num) for num in lines[i][10:39].split())
    numbers = set(int(num) for num in lines[i][42:116].split())
    match = len(numbers.intersection(winning))
    total_cards += find_cards(i, match) + 1

print(total_cards)
