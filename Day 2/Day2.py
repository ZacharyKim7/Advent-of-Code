with open('Data2.txt') as f:
    lines = [line.strip() for line in f]

# score = 0
# def first_A(pair):
#     global score
#     if pair[2] == "X":
#         score += 4
#     elif pair[2] == "Y":
#         score += 8
#     elif pair[2] == "Z":
#         score += 3

# # paper
# def first_B(pair):
#     global score
#     if pair[2] == "X":
#         score += 1
#     elif pair[2] == "Y":
#         score += 5
#     elif pair[2] == "Z":
#         score += 9

# # Scissors
# def first_C(pair):
#     global score
#     if pair[2] == "X":
#         score += 7
#     elif pair[2] == "Y":
#         score += 2
#     elif pair[2] == "Z":
#         score += 6


# for pair in lines:
#     if pair[0] == "A":
#         first_A(pair)
#     elif pair[0] == "B":
#         first_B(pair)
#     else:
#         first_C(pair)

score = 0
def lose(pair):
    global score
    if pair[0] == "A":
        score += 3
    elif pair[0] == "B":
        score += 1
    else:
        score += 2

def draw(pair):
    global score
    if pair[0] == "A":
        score += 4
    elif pair[0] == "B":
        score += 5
    else:
        score += 6
    
def win(pair): 
    global score
    if pair[0] == "A":
        score += 8
    elif pair[0] == "B":
        score += 9
    else:
        score += 7

for pair in lines:
    if pair[2] == "X":
        lose(pair)
    elif pair[2] == "Y":
        draw(pair)
    else:
        win(pair)

print(score)