def process(line):
    marker_length = 14
    for n in range(0, len(line)):
        marker = line[n:marker_length+n]
        unique = all([marker.count(x) == 1 for x in marker])
        if unique:
            print(marker)
            return n+marker_length
    return 0

def main():


    processed = 0
    with open('input/input6.txt') as f:
        for line in f:
            processed += process(line.strip())
    print(processed)


if __name__ == "__main__":
    main()
