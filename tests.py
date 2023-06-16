import os
import os.path
import shutil
import unittest

from functions import sorting_from_to, get_all_paths


msg_sorting = "Test error: {0}\npaths before:\n{1}\n paths after:\n{2}"


def _sorting_error_msg(msg, paths_before, path_after):
    return "\n\nSorting failed: \"{0}\"\n\n" \
        "paths before:\n\n{1}\n\n" \
        "paths after:\n\n{2}\n\n".format(msg, 
            "\n".join(paths_before), "\n".join(path_after))


class TestingSorted(unittest.TestCase):

    def setUp(self):
        # сохраняем начальное значение рабочей директории нужно для
        # того что бы не было путаницы при запуске из другого каталога
        self.previous_work_directory = os.getcwd()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.dir_for_testing = "test_dir"
        os.mkdir(self.dir_for_testing)

    def tearDown(self):
        # удаляем директорию в которой были файлы для сортировки
        shutil.rmtree(self.dir_for_testing)
        # возвращаем первоначальную рабочую директорию
        os.chdir(self.previous_work_directory)

    def testing_sorting_from_to(self):
        # создаём директории и файлы для сортировки
        dir_dirty = os.path.join(os.getcwd(), self.dir_for_testing, "dirty")
        dir_clean = os.path.join(os.getcwd(), self.dir_for_testing, "clean")
        os.mkdir(dir_dirty)
        os.mkdir(dir_clean)
        file_names = ("file.txt", "file.jpg")
        for file_name in file_names:
            with open(os.path.join(dir_dirty, file_name), "w"): pass
        # пути объектов и количество файлов ДО сортировки
        num_files_before = 0
        for root, dirs, files in os.walk(dir_dirty):
            num_files_before += len(files)
        paths_before = get_all_paths(self.dir_for_testing)
        # запускаем сортировку
        dirs_n_extens = (
            {"dirname": "pictures", "extensions": ["jpg"]},
            {"dirname": "text_files", "extensions": ["txt"]},
            )
        sorting_from_to(dir_dirty, dir_clean, dirs_n_extens)
        # пути объектов и количество файлов ПОСЛЕ сортировки
        paths_after = get_all_paths(self.dir_for_testing)
        num_files_after = 0
        for root, dirs, files in os.walk(dir_clean):
            num_files_after += len(files)
        # проверяем результат сортировки
        all_dirnames, all_extensions = [], []
        for dir_n_extens in dirs_n_extens:
            all_dirnames.append(dir_n_extens["dirname"])
            all_extensions += dir_n_extens["extensions"]
        # в "грязной" папке, не должно быть файлов, с расширениями
        # для сортировки
        for file in os.listdir(dir_dirty):
            if not os.path.isfile(os.path.join(dir_dirty, file)):
                continue
            file_extension = file.rsplit(".", 1)[-1]
            self.assertNotIn(file_extension, all_extensions, 
                _sorting_error_msg("Not all files sortered!",
                        paths_before, paths_after))
        # в папках для сортировки должны быть только файлы указанных
        # расширений
        for dir_n_extens in dirs_n_extens:
            # print(f"dir_n_extens: {dir_n_extens}")
            dirname = os.path.join(dir_clean, dir_n_extens["dirname"])
            # print(f"dirname: {dirname}")
            if not os.path.exists(dirname):
                continue
            for file in os.listdir(dirname):
                # print(f"file 1: {file}")
                filename = os.path.join(dirname, file)
                if not os.path.isfile(filename):
                    continue
                # print(f"file 2: {filename}")
                extensions = dir_n_extens["extensions"]
                file_extension = filename.rsplit(".", 1)[-1]
                self.assertIn(file_extension, extensions,
                    _sorting_error_msg("Wrong file extension in directory",
                        paths_before, paths_after))
        # количество файлов не должно измениться, если изменилось, значит
        # созданы лишние файлы или файлы потеряны
        self.assertEqual(num_files_before, num_files_after, 
            _sorting_error_msg("Number of files was changed",
                paths_before, paths_after))

def sorting_from_to(dir1, dir2, dirs_n_extens):
    os.mkdir(os.path.join(dir2, "pictures"))
    os.mkdir(os.path.join(dir2, "text_files"))
    filename1 = os.path.join(dir2, "pictures/file.jpg")
    filename2 = os.path.join(dir2, "text_files/file.txt")
    # filename2 = os.path.join(dir2, "pictures/file.txt")
    filename3 = os.path.join(dir2, "text_files/file1.txt")
    open(filename1, "w").close()
    open(filename2, "w").close()
    open(filename3, "w").close()
    #
    old_filename1 = os.path.join(dir1, "file.jpg")
    old_filename2 = os.path.join(dir1, "file.txt")
    os.remove(old_filename1)
    os.remove(old_filename2)
    # shutil.rmtree(os.path.join(dir2, "pictures"))
    pass


if __name__ == '__main__':
    unittest.main(exit=0)