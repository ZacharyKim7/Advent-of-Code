with open('Data1.txt') as f:
    lines = [line.strip() for line in f]

#Part 1 
# added = []
# total = 0
# for number in lines:
#     if number == "":
#         added.append(total)
#         total = 0
#     else:
#         total += int(number)

#Part 2
added = []
total = 0
for number in lines:
    if number == "":
        added.append(total)
        total = 0
    else:
        total += int(number)

top3 = []
for i in range(3):
    top3.append(max(added))
    added.remove(max(added))
print(top3)
print(sum(top3))
