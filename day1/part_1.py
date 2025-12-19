from typing import Literal


def calculate_zero_counter(rotations, start=50) -> int:
    zeroCounter = 0
    dialPointer: int = start

    for rotation in rotations:
        direction: Literal["L", "R"] = rotation[0]
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
        rotations: list[str] = [line.strip() for line in file]

    print(calculate_zero_counter(rotations))
