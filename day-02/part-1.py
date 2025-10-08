# Day 2: Red-Nosed Reports Part 1
# https://adventofcode.com/2024/day/2
# Time Complexity O(n)
# Space Complexity O(n)

def is_valid_report(report):
    is_increasing = True
    if report[0] > report[1]:
        is_increasing = False
    for i in range(len(report) - 1):
        change = report[i + 1] - report[i]
        if not is_increasing:
            change *= -1
        if change < 1 or change > 3:
            return False
    return True


def count_valid_reports(reports):
    count = 0
    for report in reports:
        if is_valid_report(report):
            count += 1
    return count


def load_input():
    reports = []
    with open("input.txt", "r") as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            reports.append(report)
    return reports


def main():
    reports = load_input()
    count = count_valid_reports(reports)
    print(count)


if __name__ == "__main__":
    main()
