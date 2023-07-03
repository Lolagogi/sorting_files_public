import os
import os.path
import shutil
from pprint import pprint


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


def sorting_from_to(from_dir, to_dir, dirs_n_extens, subdirs=False):
    """Сортируем файлы в папки с указанными для этиx папок расширениями
        пути к папкам должны быть полными (абсолютными):
        from_dir - папка с неотсортированными файлами
        to_dir - папка куда нужно сортировать
        dirs_n_extens - правила сортировки
        subdirs - искать ли файлы в подпапках
    """
    # собираем полные имена всех файлов которые подлежат сортировке
    all_extensions = []
    for dir_n_extens in dirs_n_extens:
        all_extensions += dir_n_extens["extensions"]
    filenames_for_sorting = []
    for root, dirs, files in os.walk(from_dir):
        for file in files:
            filename = os.path.join(root, file)
            file_extension = filename.rsplit(".", 1)[-1].lower()
            if file_extension in all_extensions:
                filenames_for_sorting.append(filename)
        # не собираем файлы из подпапок если это не нужно
        if not subdirs:
            break
    # создаём новые пути файлов на основе старых
    old_new_filenames = []
    for filename in filenames_for_sorting:
        for dir_n_extens in dirs_n_extens:
            file_extension = filename.rsplit(".", 1)[-1].lower()
            if file_extension in dir_n_extens["extensions"]:
                dirname = os.path.join(to_dir, dir_n_extens["dirname"])
                if not os.path.exists(dirname):
                    os.mkdir(dirname)
                file = os.path.basename(filename)
                new_filename = os.path.join(dirname, file)
                old_new_filenames.append((filename, new_filename))
    # копируем файл в новое место, и удаляем файл из старого места
    for old_filename, new_filename in old_new_filenames:
        shutil.copy(old_filename, new_filename)
        os.remove(old_filename)


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
    # function(directory, new_directory)