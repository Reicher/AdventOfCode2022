class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f'File {self.name} with size {size}'

    def __repr__(self):
        return f'{self.name} ({self.size})'


class Folder:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.files: dict[str, File] = {}
        self.folders: dict[str, Folder] = {}

    def __str__(self):
        return f'Folder {self.name} with {len(self.folders)} sub folders and {len(self.files)} files'

    def __repr__(self):
        return f'{self.name}'

    def add_file(self, file_string: str):
        size, f_name = file_string.split(' ')
        if f_name not in self.files:
            self.files[f_name] = File(f_name, int(size))

    def add_folder(self, folder_name):
        if folder_name not in self.folders:
            self.folders[folder_name] = Folder(folder_name, self)

    def get_total_size(self):
        direct_file_sizes = sum(file.size for file in self.files.values())
        indirect_file_sizes = sum(folder.get_total_size() for folder in self.folders.values())
        return direct_file_sizes + indirect_file_sizes


def sum_folders(root: Folder, tot_sum=0):
    for child in root.folders.values():
        tot_sum = sum_folders(child, tot_sum)

    folder_size = root.get_total_size()
    if folder_size <= 100000:
        #print(f'{root} under 100000! Adding {folder_size}, now total {tot_sum + folder_size}')
        return tot_sum + folder_size
    else:
        return tot_sum


def find_minimum_folder(root: Folder, to_free, best_so_far):
    for child in root.folders.values():
        best_so_far = find_minimum_folder(child, to_free, best_so_far)

    size = root.get_total_size()
    if to_free <= size < best_so_far:
        return size

    return best_so_far


def main():
    root = Folder('/', None)
    pwd = None

    with open('input/input7.txt') as f:
    #with open('input/input_sample.txt') as f:
        for line in f:
            line = line.strip()
            if line.startswith('$ '):
                cmd = line.split(' ')[1]
                if cmd == 'cd':
                    path = line.split(' ')[2]
                    if path == '/':
                        pwd = root
                    elif path == '..':
                        pwd = pwd.parent
                    else:
                        pwd = pwd.folders[path]
            elif line.startswith('dir '):
                f_name = line.split(' ')[1]
                pwd.add_folder(f_name)
            elif not line.startswith('dir '):
                pwd.add_file(line)

    # sum of all folder with total size < 100000
    print(f'Total sum of folders under 100000: {sum_folders(root)}')

    total_space = 70000000
    unused_needed = 30000000
    used_space = root.get_total_size()
    unused_space = total_space - used_space
    space_to_free = unused_needed - unused_space
    best_folder = used_space  # actually worst
    print(f'Folder size of smallest needed folder: '
          f'{find_minimum_folder(root, space_to_free, best_folder)}')


if __name__ == "__main__":
    main()
