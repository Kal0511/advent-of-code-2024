# Day 1: Historian Hysteria Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O(n log n)
# Space Complexity O(n)


def count_total_distance(l1: list[int], l2: list[int]):
    l1.sort()
    l2.sort()

    total_distance = 0
    for i in range(len(l1)):
        total_distance += abs(l1[i] - l2[i])
    return total_distance


def load_input():
    l1, l2 = [], []
    with open("input.txt", "r") as file:
        for line in file:
            n1, n2 = line.strip().split()
            l1.append(int(n1))
            l2.append(int(n2))
    return l1, l2


def main():
    l1, l2 = load_input()
    total_distance = count_total_distance(l1, l2)
    print(total_distance)


if __name__ == "__main__":
    main()
