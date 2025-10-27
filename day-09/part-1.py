# Day 9: Disk Fragmenter Part 1
# https://adventofcode.com/2024/day/1
# Time Complexity O()
# Space Complexity O()

def checksum(data):
    l = 0
    r = len(data) - 1
    last_ID = 0
    remaining_end = 0
    pos = 0
    count = 0
    while l <= r:
        ID = l / 2
        if l % 2 == 0:
            newPos = pos+int(data[l])
            print(pos,newPos)
            count += ID * sum(range(pos,newPos))
            l += 1
            pos = newPos
        else:
            size = int(data[l])
            print(pos)
            while size > 0:
                if remaining_end == 0:
                    remaining_end = int(data[r])
                    last_ID = r / 2
                    r -= 2
                if remaining_end > size:
                    count += last_ID * sum(range(pos,pos+size))
                    pos += size
                    remaining_end -= size
                    size = 0
                else:
                    count += last_ID * sum(range(pos,pos+remaining_end))
                    pos += remaining_end
                    size -= remaining_end
                    remaining_end = 0
            l += 1
            print(pos)
    count += (l+1) / 2 * sum(range(pos,pos+remaining_end))
    return count



def load_input():
    with open("input.txt", "r") as file:
        return file.read().strip()


def main():
    data = load_input()
    count = checksum(data)
    print(count)



if __name__ == "__main__":
    main()
