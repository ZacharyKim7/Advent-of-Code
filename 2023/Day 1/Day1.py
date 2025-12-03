with open("AdventOfCode23\Day 1\Jack.txt") as f:
    lines = [line.strip() for line in f]

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ints = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# final = 0
# for value in lines:
#     left_val = False
#     right_val = False
#     left = 0
#     right = -1
#     ans = []

#     while left_val != True:
#         if value[left] not in digits:
#             left += 1
#         else:
#             ans.append(value[left])
#             left_val = True
#     while right_val != True:
#         if value[right] not in digits:
#             right -= 1
#         else:
#             ans.append(value[right])
#             right_val = True
#     final += int("".join(ans))
# print(final)

final2 = 0
index = 1
for value in lines:
    left_index = 0
    right_index = -3
    right_index_right = None
    left = False
    right = False
    ans = []

    while left != True:
        if value[left_index] in digits:
            ans.append(value[left_index])
            break
        elif value[left_index:left_index + 3] in numbers:
            ans.append(ints[value[left_index:left_index + 3]])
            break
        elif value[left_index:left_index + 4] in numbers:
            ans.append(ints[value[left_index:left_index + 4]])
            break
        elif value[left_index:left_index + 5] in numbers:
            ans.append(ints[value[left_index:left_index + 5]])
            break
        left_index += 1
    
    while right != True:
        if value[right_index + 2] in digits:
            ans.append(value[right_index + 2])
            break
        elif value[right_index:right_index_right] in numbers:
            ans.append(ints[value[right_index:right_index_right]])
            break
        elif value[(right_index - 1):right_index_right] in numbers:
            ans.append(ints[value[(right_index - 1):right_index_right]])
            break
        elif value[(right_index - 2):right_index_right] in numbers:
            ans.append(ints[value[(right_index - 2):right_index_right]])
            break
        else:
            right_index -= 1
            if (right_index_right == None):    
                right_index_right = -1
            else:
                right_index_right -= 1
    final2 += int("".join(ans))
    print(index, ans)
    index += 1
print(final2)



