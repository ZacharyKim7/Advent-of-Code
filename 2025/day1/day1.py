with open("data1.txt") as f:
    lines = [line.strip() for line in f]

def part_1():
    times_zero = 0
    pos = 50

    for turn in lines:
        if turn[0:1] == "L":
            raw_pos = pos - int(turn[1:])
            if raw_pos < 0:
                pos = (100 + raw_pos) % 100
            else:
                pos = raw_pos
        else:
            raw_pos = pos + int(turn[1:])
            pos = raw_pos % 100

        if pos == 0:
            times_zero += 1

    print(times_zero)
    return times_zero

def part_2():
    times_zero = 0
    pos = 50  # starting position

    for turn in lines:
        direction = turn[0]
        steps = int(turn[1:])

        if direction == "L":
            raw_pos = pos - steps

            if raw_pos <= 0:
                # How many times do we hit 0 when moving left?
                if pos == 0:
                    # Starting on 0: only count full 100-step laps
                    crosses = (-raw_pos) // 100
                else:
                    # First time we hit 0 is after `pos` steps,
                    # then once every additional 100 steps
                    crosses = (steps - pos) // 100 + 1

                if crosses < 0:  # in case steps < pos
                    crosses = 0

                times_zero += crosses

            pos = raw_pos % 100

        else:  # direction == "R"
            raw_pos = pos + steps

            if raw_pos >= 100:
                # Each full 100-step lap to the right hits 0 once
                times_zero += raw_pos // 100

            pos = raw_pos % 100

    print(times_zero)
    return times_zero

# part_1()
part_2()