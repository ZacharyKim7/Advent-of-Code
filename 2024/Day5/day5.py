from functools import cmp_to_key

with open("data5.txt") as f:
    rules, pages = f.read().split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in rules.split("\n")]
pages = [list(map(int, line.split(","))) for line in pages.split("\n")]

comparison = cmp_to_key(lambda a, b: -1 if (a, b) in rules else 1)

answer1 = 0
answer2 = 0
for page in pages:
    if sorted(page, key = comparison) == page:
        answer1 += page[len(page) // 2]
    else:
        page.sort(key = comparison)
        answer2 += page[len(page) // 2]
        

print(answer1)
print(answer2)
