pile_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def create_piles(line,pile):
    for pn in pile_names:
        crate = line[1 + (int(pn) - 1) * 4]
        if crate != ' ':
            if pn in pile:
                pile[pn].insert(0, crate)
            else:
                pile[pn] = [crate]


def crate_9000(command, pile):
    first = command.split(' from ')[0]
    second = command.split(' from ')[1]
    moves = int(first.replace('move ', ''))
    f = second.split(' to ')[0]
    t = second.split(' to ')[1]
    for m in range(0, moves):
        pile[t].append(pile[f].pop())


def crate_9001(command, pile):
    first = command.split(' from ')[0]
    second = command.split(' from ')[1]
    crates = int(first.replace('move ', ''))
    f = second.split(' to ')[0]
    t = second.split(' to ')[1]
    stack = pile[f][-crates:]
    del pile[f][-crates:]
    pile[t] += stack


def print_top_crate(pile):
    goal = ''
    for pn in pile_names:
        goal += pile[pn][-1]
    print(goal)


def main():
    pile = {}
    with open('input/input5.txt') as f:
        for line in f:
            if '[' in line:
                create_piles(line, pile)
            elif 'move' in line:
                crate_9001(line.strip(), pile)
    print_top_crate(pile)


if __name__ == "__main__":
    main()