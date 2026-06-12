# Day 1: Secret Entrance Part 1
# https://adventofcode.com/2025/day/1
# Time Complexity O(n)
# Space Complexity O(n)


def count_zeros(rotations: list):
    i = 50
    count = 0

    for rotation in rotations:
        turn = int(rotation[1:]) % 100
        if rotation[0] == 'L':
            i -= turn
            if i < 0:
                i += 100
        else:
            i += turn
            if i > 99:
                i -= 100
        if i == 0:
            count += 1
    return count


def load_input():
    rotations = []
    # with open("input-example.txt", "r") as file:
    with open("input.txt", "r") as file:
        for line in file:
            rotations.append(line)
    return rotations


def main():
    rotations = load_input()
    password = count_zeros(rotations)
    print(password)


if __name__ == "__main__":
    main()
