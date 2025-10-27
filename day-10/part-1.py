# Day 1: Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O()
# Space Complexity O()

def count_trails(grid):
    count = 0
    return 0


def load_input():
    grid = []
    with open("input-example.txt", "r") as file:
        for line in file:
            grid.append(list(map(int, line.strip())))
    return grid


def main():
    grid = load_input()
    count = count_trails(grid)
    print(count)


if __name__ == "__main__":
    main()
