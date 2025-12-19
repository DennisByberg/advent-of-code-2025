# --- Day 1: Secret Entrance: Part 1 ---
# https://adventofcode.com/2025/day/1#part1

with open("input.txt", "r") as file:
    rotations = [line.strip() for line in file]

zeroCounter = 0
dialPointer = 50

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

# Correct answer: 1105
print(zeroCounter)
