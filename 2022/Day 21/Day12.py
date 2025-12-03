with open("Data12.txt") as f:
    lines = [line.strip() for line in f]

start = None
for line in lines:
    try:
        start = (lines.index(line), line.index("S"), 0)
    except ValueError:
        continue


queue = [start]
visited = set([])
visited.add((start[0], start[1]))
minSteps = None

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while queue:

    current = queue.pop()
    if lines[current[0]][current[1]] == 'E':
        minSteps = current[2]
        break

    for direction in directions:
      
        new_node = (current[0] + direction[0], current[1] + direction[1])

        if new_node[0] > -1 and new_node[0] < len(lines) and new_node[1] > 0 and new_node[1] < len(lines[0]):
            if lines[current[0]][current[1]] == 'S':
                goodElevation = ord('a') + 1 >= ord(lines[new_node[0]][new_node[1]])
            elif lines[new_node[0]][new_node[1]] == 'E':
                goodElevation = ord(lines[current[0]][current[1]]) >= ord('z')
            else:
                goodElevation = ord(lines[current[0]][current[1]]) + 1 >= ord(lines[new_node[0]][new_node[1]])
            
            if new_node not in visited and goodElevation:
                visited.add(new_node)
                queue.insert(0, (new_node[0], new_node[1], current[2] + 1))
       
    print(queue)
print(minSteps)
