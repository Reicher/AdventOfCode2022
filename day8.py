def main():
    with open('input/input8.txt') as f:
    #with open('input/input_sample.txt') as f:
        trees = f.readlines()
    trees = [treeline.strip() for treeline in trees]
    visible_trees = (len(trees) * 2) + (len(trees[0]) * 2) - 4
    best_scenic = 0
    for x in range(1, len(trees)-1):
        for y in range(1, len(trees[x])-1):
            tree = trees[x][y]
            scenic = 0
            to_left = trees[x][:y]
            to_right = trees[x][y+1:]
            below = ''.join([trees[i][y] for i in range(x+1, len(trees))])
            above = ''.join([trees[i][y] for i in range(0, x)])

            # Visible Trees from outside
            if all(tree > t for t in to_left) or all(tree > t for t in to_right) \
                    or all(tree > t for t in below) or all(tree > t for t in above):
                visible_trees += 1

            # Scenic score
            seen_right = 0
            for t in to_right:
                seen_right += 1
                if tree <= t:
                    break

            seen_left = 0
            for t in to_left[::-1]:
                seen_left += 1
                if tree <= t:
                    break

            seen_above = 0
            for t in above[::-1]:
                seen_above += 1
                if tree <= t:
                    break

            seen_below = 0
            for t in below:
                seen_below += 1
                if tree <= t:
                    break

            scenic = seen_above * seen_below * seen_left * seen_right
            if scenic > best_scenic:
                best_scenic = scenic

    print(f'Trees visible: {visible_trees}')
    print(f'Best Scenic score: {best_scenic}')


if __name__ == "__main__":
    main()
