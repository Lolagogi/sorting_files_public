import os.path
import tkinter 
import tkinter.filedialog as filedialog
from tkinter import ttk
from tkinter import messagebox

from frame_sorting_rules import FrameSortingRules
from functions import sorting_from_to


class SortingFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_widgets()
        self.pack_widgets()

    def create_widgets(self):
        """ Создаём виджеты"""
        self.frm_chose_paths = ttk.Frame(self)
        # поля для надписей для полей ввода
        self.lbl_inp = ttk.Label(self, text="input directory")
        self.lbl_outp = ttk.Label(self, text="output directory")
        # поля ввода для директорий
        var_str_input_folder = tkinter.StringVar()
        var_str_output_folder = tkinter.StringVar()
        self.ent_inp_dir = ttk.Entry(self, width=40,
            textvariable=var_str_input_folder)
        self.ent_outp_dir = ttk.Entry(self, width=40,
            textvariable=var_str_output_folder)
        # кнопки для просмотра директории
        self.btn_brws_inp = ttk.Button(self, text="browse...")
        self.btn_brws_outp = ttk.Button(self, text="browse...")
        self.btn_brws_inp["command"] = \
            lambda : self.chose_directory(self.ent_inp_dir)
        self.btn_brws_outp["command"] = \
            lambda : self.chose_directory(self.ent_outp_dir)
        # кнопка для запуска сортировки
        self.button_sort = ttk.Button(self, text="sort")
        self.button_sort["command"] = self.do_sorting
        # рамка с правилами сортировки
        self.frm_srt_rls = FrameSortingRules(self, width=100, height=50)
        # кнопка для добавления правила для сортировки
        self.btn_add_srt_rl = ttk.Button(self, text="add sorting rule")
        self.btn_add_srt_rl["command"] = self.add_sorting_rule
        # флаг поиска в подпапках
        self.bvar_subdirs = tkinter.BooleanVar(value=False)
        self.chkbtn_subdirs = ttk.Checkbutton(self, 
            variable=self.bvar_subdirs, 
            text="сортировать файлы в подпапках")

    def pack_widgets(self):
        """Упаковываем виджеты"""
        # рамка для упаковки виджетов для настройки опций для сортировки
        self.frm_chose_paths.pack(in_=self)
        self.lbl_inp.grid(in_=self.frm_chose_paths, row=0, column=0)
        self.lbl_outp.grid(in_=self.frm_chose_paths, row=1, column=0)
        self.ent_inp_dir.grid(in_=self.frm_chose_paths, row=0, column=1)
        self.ent_outp_dir.grid(in_=self.frm_chose_paths, row=1, column=1)
        self.btn_brws_inp.grid(in_=self.frm_chose_paths, row=0, column=2)
        self.btn_brws_outp.grid(in_=self.frm_chose_paths, row=1, column=2)
        # рамка для правил сортировки, и кнопка добавления правила
        self.frm_srt_rls.pack(in_=self)
        self.btn_add_srt_rl.pack(in_=self)
        self.chkbtn_subdirs.pack(anchor="w", side="left")
        # упаковываем кнопку для сортировки
        self.button_sort.pack(in_=self, anchor="se", side="bottom")

    def chose_directory(self, entry):
        directory = filedialog.askdirectory()
        if os.path.isdir(directory):
            entry.delete(0, tkinter.END)
            entry.insert(0, directory)

    def add_sorting_rule(self):
        self.frm_srt_rls.add_sorting_rule()

    def do_sorting(self):
        from_dir = self.ent_inp_dir.get()
        to_dir = self.ent_outp_dir.get()
        dirs_n_extens = self.frm_srt_rls.get_sorting_rules()
        subdirs = self.bvar_subdirs.get()
        try:
            sorting_from_to(from_dir, to_dir, dirs_n_extens, subdirs)
        # если возникло исключение, поднимаем его выше
        except:
            messagebox.showerror(message="Error")
            raise
        else:
            messagebox.showinfo(message="sorting is sucessfull")


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(400, 400)
    sf = SortingFrame(root)
    sf.pack(in_=root, fill="both", expand=True)
    root.mainloop()