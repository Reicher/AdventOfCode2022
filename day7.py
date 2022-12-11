def main():
    pwd = []
    folder_size: dict[str, int] = {}
    folder_files: dict[str, int] = {}
    with open('input/input7.txt') as f:
    #with open('input/input_sample.txt') as f:
        for line in f:
            line = line.strip()
            if line.startswith('$ '):
                cmd = line.split(' ')[1]
                if cmd == 'cd':
                    folder = line.split(' ')[2]
                    if folder == '..':
                        pwd.pop()
                    else:
                        pwd.append(folder)
                    print(f'cd -> {"/".join(pwd)}')
            elif not line.startswith('dir '):
                print(f"file: {line.split(' ')[1]}")
                for folder in pwd:
                    if folder not in folder_size:
                        folder_size[folder] = 0
                        folder_files[folder] = 0
                    folder_size[folder] += int(line.split(' ')[0])
                    folder_files[folder] += 1

    total_ok_size = 0
    for folder, size in folder_size.items():
        if size <= 100000:
            total_ok_size += size

    print(f'total ok size: {total_ok_size}')


if __name__ == "__main__":
    main()
