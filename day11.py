import math

class Monkey:
    def __init__(self, monkey_id: int, items: [int],
                 operation, test: int, true_monkey: int, false_monkey: int):
        self.monkey_id = monkey_id
        self.items = items
        self._operation = operation
        self.test = test
        self._true_monkey = true_monkey
        self._false_monkey = false_monkey
        self.inspected_items = 0

    def set_friends(self, monkey_pals: []):
        self._friend = monkey_pals

    def inspect(self, debug=False, part_two=True):
        if debug:
            print(f'Monkey {self.monkey_id}:')

        for item in self.items:
            if debug:
                print(f'\tMonkey inspects an item with a worry level of {item}.')
            new_item = self._operation(item)

            if not part_two:
                if debug:
                    print(f'\t\tWorry level is now {new_item}.')
                new_item = int(new_item / 3)

            if debug:
                print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {new_item}.')

            if new_item % self.test == 0:
                if debug:
                    print(f'\t\tCurrent worry level is divisible by {self.test}')
                    print(f'\t\tItem with worry level {new_item} is thrown to monkey {self._true_monkey}.')
                self._friend[self._true_monkey].items.append(new_item)
            else:
                if debug:
                    print(f'\t\tCurrent worry level is not divisible by {self.test}.')
                    print(f'\t\tItem with worry level {new_item} is thrown to monkey {self._false_monkey}.')
                self._friend[self._false_monkey].items.append(new_item)
            self.inspected_items += 1
        self.items = []

    def __str__(self):
        return f'Monkey {self.monkey_id}:\n\tStarting items: {self.items}\n' \
               f'\tOperation: {self._operation}\n\tTest: dividable by {self.test}\n' \
               f'\t\tIf True: throw to monkey {self._true_monkey}\n' \
               f'\t\tIf False: throw to monkey {self._false_monkey}\n'

    def __repr__(self):
        return f'Monkey {self._monkey_id}'


# Because fuck parsing that
def sample_monkeys() -> [Monkey]:
    return [Monkey(0, [79, 98], lambda old: old * 19, 23, 2, 3),
            Monkey(1, [54, 65, 75, 74], lambda old: old + 6, 19, 2, 0),
            Monkey(2, [79, 60, 97], lambda old: old * old, 13, 1, 3),
            Monkey(3, [74], lambda old: old + 3, 17, 0, 1)]


# Because fuck parsing that
def real_monkeys() -> [Monkey]:
    return [Monkey(0, [54, 53], lambda old: old * 3, 2, 2, 6),
            Monkey(1, [95, 88, 75, 81, 91, 67, 65, 84], lambda old: old * 11, 7, 3, 4),
            Monkey(2, [76, 81, 50, 93, 96, 81, 83], lambda old: old + 6, 3, 5, 1),
            Monkey(3, [83, 85, 85, 63], lambda old: old + 4, 11, 7, 4),
            Monkey(4, [85, 52, 64], lambda old: old + 8, 17, 0, 7),
            Monkey(5, [57], lambda old: old + 2, 5, 1, 3),
            Monkey(6, [60, 95, 76, 66, 91], lambda old: old * old, 13, 2, 5),
            Monkey(7, [65, 84, 76, 72, 79, 65], lambda old: old + 5, 19, 6, 0)]


def main():
    #monkeys = real_monkeys()
    monkeys = sample_monkeys()

    for m in monkeys:
        m.set_friends(monkeys)
        print(m)

    # find monkey lcm
    #magic_monkey_number = math.lcm(monkeys[0].test, monkeys[1].test, monkeys[2].test, monkeys[3].test)

    for round in range(1, 1001):
        for monkey in monkeys:
            monkey.inspect()
        if False:
            print(f'\nAfter round {round}, the monkeys are holding items with these worry levels:')
            for monkey in monkeys:
                print(f'Monkey {monkey.monkey_id} {monkey.items}')

    print('\n')
    inspected = []
    for monkey in monkeys:
        inspected.append(monkey.inspected_items)
        print(f'Monkey {monkey.monkey_id} inspected items {monkey.inspected_items} times.')

    # best two:
    best = max(inspected)
    inspected.remove(best)
    second_best = max(inspected)

    print(f'Monkey business: {best*second_best}')


if __name__ == "__main__":
    main()
