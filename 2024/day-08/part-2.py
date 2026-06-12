# Day 8: Resonant Collinearity Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O()
# Space Complexity O()
from collections import defaultdict


def count_locations(antennas, rows, cols):
    print(antennas, rows, cols)
    anti = set()
    for k in antennas:
        antenna = antennas[k]
        for n in range(len(antenna)):
            a = antenna[n]
            anti.add(a)
            for m in range(n + 1, len(antenna)):
                b = antenna[m]

                ab = (b[0] - a[0], b[1] - a[1])
                print(a, b, ab)
                b2 = (b[0] + ab[0], b[1] + ab[1])
                a2 = (a[0] - ab[0], a[1] - ab[1])

                while 0 <= b2[0] < rows and 0 <= b2[1] < cols:
                    anti.add(b2)
                    print(b2)
                    b2 = (b2[0] + ab[0], b2[1] + ab[1])
                # print(b2)
                while 0 <= a2[0] < rows and 0 <= a2[1] < cols:
                    anti.add(a2)
                    print(a2)
                    a2 = (a2[0] - ab[0], a2[1] - ab[1])
                # print(a2)
    print(anti)
    for j in range(cols):
        for i in range(rows):
            print('#' if (i, j) in anti else '.', end='')
        print()
    return len(anti)


def load_input():
    antennas = defaultdict(list)
    with open("input.txt", "r") as file:
        j = 0
        for line in file:
            row = line.strip()
            for i in range(len(row)):
                if row[i] != '.':
                    antennas[row[i]].append((i, j))
            j += 1
    return antennas, len(row), j


def main():
    antennas, rows, cols = load_input()
    count = count_locations(antennas, rows, cols)
    print(count)


if __name__ == "__main__":
    main()
