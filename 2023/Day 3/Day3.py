with open("AdventOfCode23\Day 3\Data3.txt") as f:
    lines = [line.strip() for line in f]


# total = 0
# for row in range(len(lines)):
#     for col in range(len(lines[0])):
#         if lines[row][col].isdigit():
#             valid = False

#             for i in range(-1, 2):
#                 for j in range(-1, 2):
#                     if ()

#     # nums = list(int(num) for num in lines[i].split('.') if num.isdigit())
#     # print(nums)


def is_symbol(c):
  return c in "*#+.$"

def get_adjacent(grid, i, j):
  result = []
  if i > 0:
    result.append(grid[i-1][j])
    if j > 0:
      result.append(grid[i-1][j-1])
    if j < len(grid[0]) - 1:
      result.append(grid[i-1][j+1])
  if i < len(grid) - 1:
    result.append(grid[i+1][j])
    if j > 0:
      result.append(grid[i+1][j-1])
    if j < len(grid[0]) - 1:
      result.append(grid[i+1][j+1])
  if j > 0:
    result.append(grid[i][j-1])
  if j < len(grid[0]) - 1:
    result.append(grid[i][j+1])
  return result

def get_part_numbers(grid):
  result = []
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j].isdigit() and any(is_symbol(c) for c in get_adjacent(grid, i, j)):
        result.append(int(grid[i][j]))
  return result

def main():
  grid = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
  ]
  part_numbers = get_part_numbers(grid)
  print(sum(part_numbers))

if __name__ == "__main__":
  main()