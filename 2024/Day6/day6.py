with open("data6.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def part_one(lines):
    pos = (0, 0)
    obstacles = set()
    direction = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^":
                pos = (i, j)
            elif lines[i][j] == "#":
                obstacles.add((i, j))
                
    directions = {
        0:(-1, 0), # up
        1:(0, 1), # right
        2:(1, 0), # down
        3:(0, -1) # left
    }

    tiles = 0
    visited = set()

    while 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[pos[0]]):
        next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

        if next_pos in obstacles:
            direction = (direction + 1) % 4
        elif next_pos in visited:
            pos = next_pos
        else:
            pos = next_pos
            visited.add(pos)
            tiles += 1 
    return tiles

def part_two(lines):
    pos = (0, 0)
    start = (0, 0)
    obstacles = set()
    direction = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^":
                pos = (i, j)
                start = (i, j)
            elif lines[i][j] == "#":
                obstacles.add((i, j))
                
    directions = {
        0:(-1, 0), # up
        1:(0, 1), # right
        2:(1, 0), # down
        3:(0, -1) # left
    }

    valid_obstacles = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            pos = start
            direction = 0
            visited = set()
            if lines[i][j] == ".":
               obstacles.add((i, j))

            while 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[pos[0]]):
                next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

                if next_pos in obstacles:
                    direction = (direction + 1) % 4
                elif (next_pos[0], next_pos[1], direction) in visited:
                    valid_obstacles += 1
                    break
                else:
                    pos = next_pos
                    visited.add((pos[0], pos[1], direction))

            if lines[i][j] == ".":
               obstacles.remove((i, j))

    return valid_obstacles

print(part_one(lines))
print(part_two(lines))