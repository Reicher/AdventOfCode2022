def find_bad_item(rucksack):
    comp_size = int(len(rucksack) / 2)
    comp1 = rucksack[:comp_size]
    comp2 = rucksack[comp_size:]
    for item in comp1:
        if item in comp2:
            return item


def get_item_prio(item):
    if item.islower():
        return ord(item)-96
    elif item.isupper():
        return ord(item) - 38


def find_common_item(r1, r2, r3):
    for i in r1:
        if i in r2 and i in r3:
            return i

def main():
    with open('input/input3.txt') as f:
        sum_of_prios = 0
        elf_group = []

        for line in f:
            rucksack = line.strip()
            elf_group.append(rucksack)

            if len(elf_group) == 3:
                badge = find_common_item(elf_group[0], elf_group[1], elf_group[2])
                print(elf_group)
                prio = get_item_prio(badge)
                sum_of_prios += prio
                elf_group = []
                print(f'Badge: {badge}. Prio {prio}')
        print(f'sum of badges: {sum_of_prios}')


if __name__ == "__main__":
    main()