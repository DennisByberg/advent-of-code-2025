# --- Day 1: Secret Entrance - Part 2 ---


def calculate_zero_counter_click(rotations, start=50):
    zeroCounter = 0
    dialPointer = start

    for rotation in rotations:
        direction = rotation[0]
        number = int(rotation[1:])

        if direction == "R":
            for i in range(number):
                dialPointer += 1
                if dialPointer == 100:
                    dialPointer = 0
                if dialPointer == 0:
                    zeroCounter += 1

        if direction == "L":
            for i in range(number):
                dialPointer -= 1
                if dialPointer == -1:
                    dialPointer = 99
                if dialPointer == 0:
                    zeroCounter += 1

    return zeroCounter


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        rotations = [line.strip() for line in file]

    print(calculate_zero_counter_click(rotations))
