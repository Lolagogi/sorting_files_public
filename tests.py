import os
import os.path
import shutil
import unittest

from functions import sorting_from_to

msg_not_all_sortered = """\
Not all files sortered!
"""
msg_wrong_extension_in_dir = """\
Wrong extension in directory
"""

class TestingSorted(unittest.TestCase):

    def setUp(self):
        # сохраняем начальное значение рабочей директории
        # нужно для того что бы не было путаницы при запуске из другого
        # каталога
        self.previous_work_directory = os.getcwd()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.dir_for_testing = "for_testing_of_sorting"
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
        # запускаем сортировку
        dirs_n_extens = (
            {"dirname": "pictures", "extensions": ["jpg"]},
            {"dirname": "text_files", "extensions": ["txt"]},
            )
        sorting_from_to(dir_dirty, dir_clean, dirs_n_extens)
        # проверяем результат сортировки
        all_dirnames, all_extensions = [], []
        for dir_n_extens in dirs_n_extens:
            all_dirnames.append(dir_n_extens["dirname"])
            all_extensions += dir_n_extens["extensions"]
        # в папках для сортировки должны быть только файлы указанных
        # расширений
        for dir_n_extens in dirs_n_extens:
            dirname = os.path.join(dir_clean, dir_n_extens["dirname"])
            if not os.path.exists(dirname):
                continue
            for file in os.listdir(dirname):
                if not os.path.isfile(file):
                    continue
                extensions = dir_n_extens["extensions"]
                file_extension = file.rsplit(".", 1)[-1]
                self.assertIn(file_extension, extensions, 
                    msg_wrong_extension_in_dir)
        # в "грязной" папке, не должно быть файлов, с расширениями
        # для сортировки
        for file in os.listdir(dir_dirty):
            if not os.path.isfile(os.path.join(dir_dirty, file)):
                continue
            file_extension = file.rsplit(".", 1)[-1]
            self.assertNotIn(file_extension, all_extensions, 
                msg_not_all_sortered)


if __name__ == '__main__':
    unittest.main(exit=0)