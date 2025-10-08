# Day 3: Mull It Over Part 2
# https://adventofcode.com/2024/day/3
# Time Complexity O(n)
# Space Complexity O(n)

import re


def calculate_multiplications(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"(do\(\)|don't\(\))"
    matches = re.findall(f"{control_pattern}|{pattern}", data)

    result = 0
    mul_enabled = True

    for match in matches:
        if match[0]:
            mul_enabled = match[0] == "do()"
        elif mul_enabled:
            result += int(match[1]) * int(match[2])
    return result


def load_input():
    with open("input.txt", "r") as file:
        return file.read()


def main():
    data = load_input()
    count = calculate_multiplications(data)
    print(count)


if __name__ == "__main__":
    main()
