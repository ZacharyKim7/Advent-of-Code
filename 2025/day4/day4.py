def p1():
    with open("data4.txt") as f:
        lines = [line.strip() for line in f]

    def isValidRoll(r, c, n_rows, n_cols):
        to_check = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
        count = 0
        for r1, c1 in to_check:
            if 0 <= r1 < n_rows and 0 <= c1 < n_cols and lines[r1][c1] == "@":
                count += 1
        
        if count < 4:
            return True
        else:
            return False

    valid_rolls = 0
    n_rows = len(lines)
    n_cols = len(lines[0])

    for row in range(n_rows):
        for col in range(n_cols):
            if lines[row][col] == "@" and isValidRoll(row, col, n_rows, n_cols):
                valid_rolls += 1
    
    print(valid_rolls)
    return valid_rolls

def p2():
    with open("data4.txt") as f:
        lines = [line.strip() for line in f]

    def isValidRoll(grid, r, c, n_rows, n_cols):
        to_check = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
        count = 0
        for r1, c1 in to_check:
            if 0 <= r1 < n_rows and 0 <= c1 < n_cols and grid[r1][c1] == "@":
                count += 1
        
        if count < 4:
            return True
        else:
            return False

    total_rolls = 0
    n_rows = len(lines)
    n_cols = len(lines[0])

    grid = [[char for char in line] for line in lines]
    last_count = 0
    doneRemoving = False

    while not doneRemoving:
        valid_rolls = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == "@" and isValidRoll(grid, row, col, n_rows, n_cols):
                    valid_rolls += 1
                    grid[row][col] = "."
        if valid_rolls == last_count:
            doneRemoving = True
        else:
            total_rolls += valid_rolls

    print(total_rolls)
    return total_rolls

p1()
p2()
