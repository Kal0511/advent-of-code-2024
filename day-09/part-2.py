# Day 9: Disk Fragmenter Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O()
# Space Complexity O()

def checksum(data):
    id = 0
    block_disk_map = []
    position = 0

    block_state = True
    for index in range(len(data)):
        if block_state:
            token = id
            id += 1
            block_state = False
        else:
            token = -1
            block_state = True

        block_disk_map.append(([token, int(data[index]), position]))
        position += int(data[index])

    positive_block_indices = [i for i, x in enumerate(block_disk_map) if x[0] >= 0]

    for positive_block_index in reversed(positive_block_indices):
        for neg_block_index in range(positive_block_index):
            if block_disk_map[neg_block_index][0] == -1:

                diff = block_disk_map[neg_block_index][1] - block_disk_map[positive_block_index][1]
                if diff >= 0:
                    block_disk_map[neg_block_index][1] = diff
                    block_disk_map[positive_block_index][2] = block_disk_map[neg_block_index][2]
                    block_disk_map[neg_block_index][2] += block_disk_map[positive_block_index][1]

                    break



    # compute the checksum
    sum = 0
    for block in block_disk_map:
        if block[0] >= 0:
            sum += block[0]*(block[1]*block[2] + ((block[1]-1)*block[1])//2)

    return sum


def load_input():
    with open("input.txt", "r") as file:
        return file.read().strip()


def main():
    data = load_input()
    count = checksum(data)
    print(count)



if __name__ == "__main__":
    main()
