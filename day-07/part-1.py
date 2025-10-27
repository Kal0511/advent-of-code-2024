# Day 7: Bridge Repair Part 1
# https://adventofcode.com/2024/day/7
# Time Complexity O()
# Space Complexity O()
def is_valid(equation, total, i):
    if i == 1:
        return total == equation[1]
    if total % equation[i] == 0 and is_valid(equation, total // equation[i], i - 1):
        return True
    elif total - equation[i] >= equation[1] and is_valid(equation, total - equation[i], i - 1):
        return True
    return False


def calculate_calibration_result(equations):
    count = 0
    for equation in equations:
        if is_valid(equation, equation[0], len(equation) - 1):
            count += equation[0]
    return count


def load_input():
    equations = []
    with open("input.txt", "r") as file:
        for line in file:
            equation = []
            parts = line.strip().split(': ')
            equation.append(int(parts[0]))
            equation.extend(map(int, parts[1].split()))
            equations.append(equation)
    return equations


def main():
    grid = load_input()
    count = calculate_calibration_result(grid)
    print(count)


if __name__ == "__main__":
    main()
