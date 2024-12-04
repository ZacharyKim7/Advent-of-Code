with open("data4.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def part_one(lines):
    word = "XMAS"
    grid = lines
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-right
        (-1, -1), # Up-left
        (1, -1),  # Down-left
        (-1, 1)   # Up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    answer = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:  # Start search if first character matches
                for dx, dy in directions:
                    if search(i, j, dx, dy):
                        count += 1
    
    return answer

def part_two(lines):
    def is_valid(x, y):
        return 0 < x < rows - 1 and 0 < y < cols - 1
    
    def check_mas_cross(x, y):
        try:
            if (((grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S') or (grid[x - 1][y + 1] == 'S' and grid[x + 1][y - 1] == 'M')) and 
                ((grid[x - 1][y - 1] == 'M' and grid[x + 1][y + 1] == 'S') or (grid[x - 1][y - 1] == 'S' and grid[x + 1][y + 1] == 'M'))):
                return 1
            else:
                return 0
        except:
            return 0
        
    grid = lines
    rows, cols = len(grid), len(grid[0])
    answer = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A' and is_valid(i, j):
                answer += check_mas_cross(i, j)

    return answer
    
print(part_one(lines))
print(part_two(lines))
