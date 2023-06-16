import os
import shutil

def function(directory, new_derictory):
    for file_name in os.listdir(directory):
        if file_name.endswith(".jpg"):
            first_word = file_name.split(" ", 1)[0].split("(")[0].split(".")[0].split("_")[0]
            new_folder = new_directory + first_word
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
                shutil.copy(directory + file_name, new_folder + "\\" + file_name)
            else:
                shutil.copy(directory + file_name, new_folder + "\\" + file_name)


def sorting_from_to(from_dir, to_dir, dirs_n_extens):
    pass

def get_all_paths(dirname):
    """Возвращает пути всех объектов в каталоге"""
    all_paths = set()
    for root, directories, files in os.walk(dirname):
        for directory in directories:
            all_paths.add(os.path.join(root, directory))
        for file in files:
            all_paths.add(os.path.join(root, file))
    return sorted(list(all_paths))


if __name__ == '__main__':
    directory = "E:\\code\\sort_folders\\foto-filtry-nordfil\\"
    new_directory = "E:\\code\\sort_folders\\foto-filtry-nordfil-go\\"
    function(directory, new_directory)
    print(get_all_paths(r"D:\files - копия (2)"))
