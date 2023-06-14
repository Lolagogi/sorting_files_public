import os
import os.path
import shutil
import unittest

from functions import 


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
        dir_dirty = os.path.join(os.getcwd(), self.dir_for_testing, "dirty")
        dir_clean = os.path.join(os.getcwd(), self.dir_for_testing, "clean")
        file_names = ("file.txt", "file.jpg")
        for file_name in file_names:
            with open(os.path.join(dir_dirty, file_name), "w"): pass

        # self.assertTrue(False)
        pass


if __name__ == '__main__':
    unittest.main(exit=0)