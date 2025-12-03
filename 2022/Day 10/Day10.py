with open("Data10.txt") as f:
    lines = [line.strip() for line in f]

changes = []
for line in lines:
    changes.append(0)
    if line[:4] == "addx":
        changes.append(int(line[5:]))

cycles = {}
for i in range(len(changes)):
    cycles[i] = changes[i]

ans = 0
val = 1

for i in range(len(changes)):
    if i % 40 == 20:
        ans += i * val
    val += changes[i]

print(ans)


#part 2

with open("result.txt", 'w') as f:

    row = ""
    val = 1

    for i in range(len(changes)):
        # print("Cycle:",i+1)
        # print("X:", val)
        # print("Position:",len(row))
        # print()
        if abs(val - len(row)) < 2:
            row += '#'
        else:
            row += '.'

        val += changes[i]

        if (i+1) % 40 == 0 and i != 0:
            print(i)
            f.write(row + '\n')
            row = ""


        

