with open('Data8.txt') as f:
    lines = [line.strip() for line in f]


def count_visible_trees(lines):
    visible = 392
    for x in range(1, len(lines)-1):
        for y in range(1, len(lines[0])-1):
            
            # to the left
            if all(lines[x][y] > lines[x][i] for i in range(y)):
                visible += 1
                continue

            # to the right
            if all(lines[x][y] > lines[x][i] for i in range(y + 1, len(lines[0]))):
                visible += 1
                continue

            # from top
            if all(lines[x][y] > lines[i][y] for i in range(x)):
                visible += 1
                continue

            # from bottom
            if all(lines[x][y] > lines[i][y] for i in range(x + 1, len(lines))):
                visible += 1
                continue
    return visible

print(count_visible_trees(lines))

def scenic_score(lines):
    highest_score = 0
    for x in range(1, len(lines)-1):
        for y in range(1, len(lines[0])-1):

            score_left = 1
            for i in range(y - 1, 0, -1):
                if lines[x][i] >= lines[x][y]:
                    break
                score_left += 1
                
            score_right = 1
            for i in range(y + 1, len(lines[0]) - 1):
                if lines[x][i] >= lines[x][y]:
                    break
                score_right +=1

            score_up = 1
            for i in range(x - 1, 0, -1):
                if lines[i][y] >= lines[x][y]:
                    break
                score_up += 1

            score_down = 1
            for i in range(x + 1, len(lines) - 1):
                if lines[i][y] >= lines[x][y]:
                    break
                score_down += 1

            score = score_up * score_down * score_left * score_right
            highest_score = max(highest_score, score)
    return highest_score
    
print(scenic_score(lines))

