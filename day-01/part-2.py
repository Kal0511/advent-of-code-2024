# Day 1: Historian Hysteria Part 2
# https://adventofcode.com/2024/day/1
# Time Complexity O(n)
# Space Complexity O(n)

from collections import defaultdict


def count_similarity(l1: list[int], l2: list[int]):
    l2_count = defaultdict(int)
    for n2 in l2:
        l2_count[n2] += 1

    similarity = 0
    for n1 in l1:
        similarity += n1 * l2_count[n1]
    return similarity


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
    similarity = count_similarity(l1, l2)
    print(similarity)


if __name__ == "__main__":
    main()
