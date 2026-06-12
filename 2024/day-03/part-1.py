# Day 3: Mull It Over Part 1
# https://adventofcode.com/2024/day/3
# Time Complexity O(n)
# Space Complexity O(n)

import re


def calculate_multiplications(data):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return sum(int(x) * int(y) for x, y in matches)


def load_input():
    with open("input.txt", "r") as file:
        return file.read()


def main():
    data = load_input()
    count = calculate_multiplications(data)
    print(count)


if __name__ == "__main__":
    main()
