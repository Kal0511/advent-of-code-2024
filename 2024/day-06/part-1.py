# Day 1: Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O()
# Space Complexity O()

def find_guard(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == "^":
                return i, j
    return 0, 0


def march(grid):
    i, j = find_guard(grid)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0
    count = 1
    while 0 < i < len(grid[0]) - 1 and 0 < j < len(grid) - 1:
        dj, di = directions[direction]
        newJ, newI = j + dj, i + di
        if grid[newJ][newI] == "#":
            direction = (direction + 1) % 4
        else:
            i, j = newI, newJ
            if grid[j][i] == ".":
                count += 1
                grid[j][i] = None
    return count


def load_input():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def main():
    grid = load_input()
    count = march(grid)
    print(count)


if __name__ == "__main__":
    main()
