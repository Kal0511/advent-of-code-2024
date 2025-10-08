# Day 4: Ceres Search Part 2
# https://adventofcode.com/2024/day/4
# Time Complexity O(n^2) (rows * columns)
# Space Complexity O(n^2)

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])

    def checker(x, y):
        part1 = False
        part2 = False

        # Top right to bottom left
        if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
            part1 = True
        elif grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M":
            part1 = True

        # Top left to bottom right
        if grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S":
            part2 = True
        elif grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M":
            part2 = True

        return part1 and part2

    counter = 0
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] != 'A':
                continue
            if checker(x, y):
                counter += 1
    return counter


def load_input():
    grid = []
    with open("part-2-input.txt", "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def main():
    grid = load_input()
    count = count_x_mas(grid)
    print(count)


if __name__ == "__main__":
    main()
