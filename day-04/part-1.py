# Day 4: Ceres Search Part 2
# https://adventofcode.com/2024/day/4
# Time Complexity O(n^2) (rows * columns)
# Space Complexity O(n^2)


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = ['X', 'M', 'A', 'S']
    word_length = len(word)
    directions = [
        (0, 1),  # Up
        (0, -1),  # Down
        (-1, 0),  # Left
        (1, 0),  # Right
        (1, 1),  # Up Right
        (1, -1),  # Down Right
        (-1, -1),  # Down Left
        (-1, 1)  # Up Left
    ]

    def checker(x, y, dx, dy):
        for i in range(1, word_length):
            newX = x + i * dx
            newY = y + i * dy

            # Check if not out of bounds
            if not ((0 <= newX < rows) and (0 <= newY < cols)):
                return False

            # Check if char doesnt match
            if grid[newX][newY] != word[i]:
                return False

        return True

    counter = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != 'X':
                continue
            for dx, dy in directions:
                if checker(x, y, dx, dy):
                    counter += 1
    return counter


def load_input():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def main():
    grid = load_input()
    count = count_xmas(grid)
    print(count)


if __name__ == "__main__":
    main()
