with open('Data5.txt') as f:
     lines = [line.strip() for line in f]

stacks = {
    1: [["L"], ["C"], ["G"], ["M"], ["Q"]],
    2: [["G"], ["H"], ["F"], ["T"], ["C"], ["L"], ["D"], ["R"]],
    3: [["R"], ["W"], ["T"], ["M"], ["N"], ["F"], ["J"], ["V"]],
    4: [["P"], ["Q"], ["V"], ["D"], ["F"], ["J"]],
    5: [["T"], ["B"], ["L"], ["S"], ["M"], ["F"], ["N"]],
    6: [["P"], ["D"], ["C"], ["H"], ["V"], ["N"], ["R"]],
    7: [["T"], ["C"], ["H"]],
    8: [["P"], ["H"], ["N"], ["Z"], ["V"], ["J"], ["S"], ["G"]],
    9: [["G"], ["H"], ["F"], ["Z"]]
}

# for string in lines: 
#     separated = string.split(" ")
#     positions = []
#     for piece in separated:
#         try:
#             positions.append(int(piece))
#         except ValueError:
#             continue
#     number, start, end = positions[0], positions[1], positions[2]
#     for j in range(1, number + 1):
#         take = stacks[start][0]
#         stacks[start].remove(stacks[start][0])
#         stacks[end].insert(0, take)


# Part 2
# for string in lines: 
#     separated = string.split(" ")
#     positions = []
#     for piece in separated:
#         try:
#             positions.append(int(piece))
#         except ValueError:
#             continue
#     switch = []
#     number, start, end = positions[0], positions[1], positions[2]
#     for j in range(1, number + 1):
#         take = stacks[start][0]
#         stacks[start].remove(stacks[start][0])
#         switch.insert(0, take)
#     for character in switch:
#         stacks[end].insert(0, character)

for i in range(1,10):
    print(stacks[i][0])