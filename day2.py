def get_points(game):
    if game == "A X":   return 1 + 3
    elif game == "B X": return 1
    elif game == "C X": return 1 + 6

    elif game == "A Y": return 2 + 6
    elif game == "B Y": return 2 + 3
    elif game == "C Y": return 2

    elif game == "A Z": return 3
    elif game == "B Z": return 3 + 6
    elif game == "C Z": return 3 + 3
    return 0


def get_move(game):
    if game == "A X":   return 'Z'
    elif game == "B X": return 'X'
    elif game == "C X": return 'Y'

    elif game == "A Y": return 'X'
    elif game == "B Y": return 'Y'
    elif game == "C Y": return 'Z'

    elif game == "A Z": return 'Y'
    elif game == "B Z": return 'Z'
    elif game == "C Z": return 'X'
    return 'FEL'

def main():
    points = 0
    with open('input/input2.txt') as f:
        for line in f:
            game = line.strip()
            move = get_move(game)
            new_game = game.split(' ')[0] + ' ' + move
            print(new_game)
            points += get_points(new_game)

    print(f'points: {points}')


if __name__ == "__main__":
    main()