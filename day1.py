def sample_input():
    sample = "1000" \
             "2000" \
             "3000" \
             "\n4000" \
             "\n5000" \
             "6000" \
             "\n7000" \
             "8000" \
             "9000" \
             "/n10000"
    return sample


def main():
    elfs = []
    food = []
    with open('input/input1.txt') as f:
        for line in f:
            if line != '\n':
                food += [int(line.strip())]
            else:
                elfs.append(food)
                food = []

    elfs_sum = []
    for elf in elfs:
        elfs_sum.append(sum(elf))

    top_3_sum = 0
    for i in range(0, 3):
        best_elf = elfs_sum.index(max(elfs_sum))
        top_3_sum += elfs_sum[best_elf]
        del elfs_sum[best_elf]

    print(f'Top 3 elfs have {top_3_sum} calories')


if __name__ == "__main__":
    main()