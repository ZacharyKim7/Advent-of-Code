with open("data2.txt") as f:
    lines = [line.strip() for line in f]

ids = lines[0].split(",")

def part_1():
    invalid = 0
    for id in ids:
        start, end = id.split("-")

        for n in range(int(start), int(end) + 1):
            s = str(n)
            l = len(s)
            if l % 2 == 0 and s[:(l//2)] == s[(l//2):]:
                invalid += int(s)
    
    print(invalid)
    return invalid

def part_2():
    def is_repeating_substring(s: str) -> bool:
        n = len(s)
        for l in range(1, n // 2 + 1):
            if n % l == 0 and s[:l] * (n // l) == s:
                return True
        return False

    invalid = 0
    for id in ids:
        start, end = id.split("-")

        for n in range(int(start), int(end) + 1):
            if is_repeating_substring(str(n)):
                invalid += n
    
    print(invalid)
    return invalid

# part_1()
part_2()
