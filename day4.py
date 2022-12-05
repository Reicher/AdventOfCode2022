def expand_tasks(desc):
    start = int(desc.split('-')[0])
    end = int(desc.split('-')[1])
    t = [start, end]
    return t


def find_fully_contained(elf1, elf2):
    elf1_tasks = expand_tasks(elf1)
    elf2_tasks = expand_tasks(elf2)
    print(f'{elf1_tasks}   {elf1_tasks}')
    if elf1_tasks[0] <= elf2_tasks[0] and elf1_tasks[1] >= elf2_tasks[1]:
        return True
    elif elf2_tasks[0] <= elf1_tasks[0] and elf2_tasks[1] >= elf1_tasks[1]:
        return True
    else:
        return False


def find_overlapping_pairs(elf1, elf2):
    elf1_tasks = expand_tasks(elf1)
    elf2_tasks = expand_tasks(elf2)
    for e1 in range(elf1_tasks[0], elf1_tasks[1]+1):
        if e1 in range(elf2_tasks[0], elf2_tasks[1]+1):
            return True


def main():
    bad = 0
    with open('input/input4.txt') as f:
        for line in f:
            task = line.strip().split(',')
            if find_overlapping_pairs(task[0], task[1]):
                print(f'{line.strip()} have overlapping tasks')
                bad += 1
            else:
                print(f'{line.strip()} doesnt have overlapping tasks')

    print(f'bad: {bad}')


if __name__ == "__main__":
    main()