with open("AdventOfCode23\Day 2\Data2.txt") as f:
    lines = [line.strip() for line in f]

total = 0
total_power = 0
id = 1
for line in lines:
    valid = True
    red, blue, green = [],[],[]
    # id = line[5:7].strip()
    draws = line[9:].split(";")
    for draw in draws:
        # print(draw.strip())
        play = draw.split(",")
        for dice in play:
            real = dice.strip()
            if real[-3:] == "red":
                red.append(int(real[0:2]))
                if int(real[0:2]) > 12:
                    valid = False
            elif real[-5:] == "green":
                green.append(int(real[0:2]))
                if int(real[0:2]) > 13:
                    valid = False
            elif real[-4:] == "blue":
                blue.append(int(real[0:2]))
                if int(real[0:2]) > 14:
                    valid = False
            else:
                continue
    if valid == True:
        total += id
    id += 1
    print(red, blue, green)
    print(max(red, default = 0) * max(blue, default = 0) * max(green, default = 0))
    total_power = total_power + max(red, default = 0) * max(blue, default = 0) * max(green, default = 0)
    print(total_power)
    
print(total)
#print(total_power)
            

            
