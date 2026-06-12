# Day 5: Print Queue Part 1
# https://adventofcode.com/2024/day/5
# Time Complexity O()
# Space Complexity O()

from collections import defaultdict
from functools import cmp_to_key


def count_total(page_pairs, updates):
    pairs = defaultdict(set)

    for page_pair in page_pairs:
        pairs[page_pair[0]].add(page_pair[1])

    def is_valid(data):
        for i in range(len(data) - 1):
            if data[i + 1] not in pairs[data[i]]:
                return False
        return True

    count = 0
    for update in updates:
        if not is_valid(update):
            update.sort(key=cmp_to_key(lambda x, y: -1 if y in pairs[x] else 1))
            count += int(update[len(update) // 2])
    return count


def load_input():
    page_pairs = []
    updates = []
    with open("input.txt", "r") as file:
        line = file.readline()
        while line:
            if line.strip() == '':
                break
            page_pairs.append(line.strip().split('|'))
            line = file.readline()

        line = file.readline()
        while line:
            updates.append(line.strip().split(','))
            line = file.readline()
    return page_pairs, updates


def main():
    page_pairs, updates = load_input()
    count = count_total(page_pairs, updates)
    print(count)


if __name__ == "__main__":
    main()
