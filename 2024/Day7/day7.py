with open("data7.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# def isValidCalibration(target, numbers):
#     def backtrack(current_value, index, prev_num):
#         # Base case: if we reach the target
#         if current_value == target and index == len(numbers):
#             return True
#         # Base case: if we've used all numbers
#         if index == len(numbers):
#             return False
        
#         # Recursive case: try addition, multiplication, and concatenation
#         next_num = int(numbers[index])
        
#         # Try addition
#         if backtrack(current_value + next_num, index + 1, next_num):
#             return True
        
#         # Try multiplication
#         if backtrack(current_value * next_num, index + 1, next_num):
#             return True
        
#         # Try concatenation
#         concatenated_num = int(str(prev_num) + str(next_num))
#         if backtrack(current_value - prev_num + concatenated_num, index + 1, concatenated_num):
#             return True
        
#         return False

#     # Start the backtracking process
#     return backtrack(0, 0, 0)

# answer = 0
# for line in lines:
#     data = line.split(" ")
#     number = int(data[0][:-1])
#     components = data[1:]

#     if isValidCalibration(number, components):
#         answer += number

# print(answer)

def eval(ns, r, t, i, ops):
    if i == len(ns):
        return r == t
    if r > t:
        return False

    for op in ops:
        nxt = r
        if op == "+":
            nxt += ns[i]
        elif op == "*":
            nxt *= ns[i]
        elif op == "||":
            nxt = int(str(nxt) + str(ns[i]))
        if eval(ns, nxt, t, i + 1, ops):
            return True

    return False


p1 = 0
p2 = 0
for line in lines:
    data = line.split(" ")
    target = int(data[0][:-1])
    rest = [int(x) for x in data[1:]]
    if eval(rest, int(rest[0]), target, 1, ["+", "*"]):
        p1 += target
    if eval(rest, int(rest[0]), target, 1, ["+", "*", "||"]):
        p2 += target


print(p1)
print(p2)