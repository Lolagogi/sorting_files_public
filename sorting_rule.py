import os
import os.path


class SortingRule:

    def is_valid(self):
        """Проверяет отвечает ли файл правилу или нет"""
        raise NotImplemented

    def make_new_filename(self):
        """Создаёт новый путь для файла"""
        raise NotImplemented


class SimpleSortingRule(SortingRule):

    def __init__(self, dirname, extensions):
        """Правило для сортировки"""
        self.dirname = dirname
        self.extensions = extensions

    def is_valid(self, filename):
        """Проверяет отвечает ли файл правилу или нет"""
        file_extension = filename.rsplit(".", 1)[-1]
        if not file_extension in dir_n_extens["extensions"]:
            return False
        return True

    def make_new_filename(self, filename):
        file = os.path.basename(filename)
        new_filename = os.path.join(dirname, file)



if __name__ == '__main__':
    sr = SimpleSortingRule("pictures", ["jpg", "jpeg"])