with open("data3.txt") as f:
    lines = [line.strip() for line in f]

def part_1():
    joltage = 0
    
    for bank in lines:
        left_max = '0'
        left_idx = 0
        right_max = '0'

        for i in range(len(bank)):
            battery = bank[i]
            if battery > left_max and i < len(bank) - 1:
                left_max = battery
                left_idx = i
                right_max = '0'

            elif battery > right_max:
                right_max = battery

        bank_total = left_max + right_max
        print(bank_total)
        joltage += int(bank_total)

    # print("total:", joltage)
    return joltage

def part_2():
    def max_k_digit_subsequence(num_str: str) -> str:
        n = len(num_str)
        k = 12

        to_remove = n - k
        stack = []

        for d in num_str:
            # While we can still remove digits and the last digit in the stack
            # is smaller than the current one, pop it to make the number larger.
            while to_remove > 0 and stack and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        # If we still need to remove digits, remove from the end
        if to_remove > 0:
            stack = stack[:-to_remove]

        # Take the first k digits (stack might be exactly length k already)
        return ''.join(stack[:k])

    joltage = 0
    for bank in lines:
        joltage += int(max_k_digit_subsequence(bank))
    
    print(joltage)
    return joltage

# part_1()
part_2()