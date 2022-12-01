with open("input/1.txt") as f:
    elves = list(map(lambda x: list(map(int, x.splitlines())), f.read().split("\n\n")))

sums = []
for elf in elves:
    sums.append(sum(elf))
sums.sort()


def part_one():
    return sums[-1]


def part_two():
    return sum(sums[-3:])


print(part_one())
print(part_two())
