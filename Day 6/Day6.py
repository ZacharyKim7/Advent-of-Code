with open('Data6.txt') as f:
     lines = [line.strip() for line in f]

possible = []
for i in range(len(lines[0]) - 14):
    seen = []
    for j in range(i, i + 14):
        seen.append(lines[0][j])
    if len(set(seen)) == 14:
        possible.append(seen)


index = []
for list in possible:
    index.append(lines[0].index("".join(list)) + 14)

print(min(index))

