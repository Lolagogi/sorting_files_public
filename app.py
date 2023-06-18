import os.path
import tkinter 
import tkinter.filedialog as filedialog
from tkinter import ttk

from frame_sorting_rules import FrameSortingRules


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
        # рамка с правилами сортировки
        self.frm_srt_rls = FrameSortingRules(self, width=100, height=50)
        # кнопка для добавления правила для сортировки
        self.btn_add_srt_rl = ttk.Button(self, text="add sorting rule")


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
        # 
        self.frm_srt_rls.pack(in_=self)
        self.btn_add_srt_rl.pack(in_=self)
        # упаковываем кнопку для сортировки
        self.button_sort.pack(in_=self, anchor="se", side="bottom")

    def chose_directory(self, entry):
        directory = filedialog.askdirectory()
        if os.path.isdir(directory):
            entry.delete(0, tkinter.END)
            entry.insert(0, directory)

    def add_sorting_rule(self):
        wnd_ask_srt_rule = tkinter.Toplevel(self)
        # wnd_ask_srt_rule.wait_window(
        pass


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(400, 400)
    sf = SortingFrame(root)
    sf.pack(in_=root, fill="both", expand=True)
    root.mainloop()