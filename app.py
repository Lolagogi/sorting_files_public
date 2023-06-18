import os.path
import tkinter 
import tkinter.filedialog as filedialog
from tkinter import ttk


class SortingFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # поля для надписей для полей ввода
        self.label_input = ttk.Label(self, text="input directory")
        self.label_output = ttk.Label(self, text="output directory")
        self.label_input.grid(in_=self, row=0, column=0)
        self.label_output.grid(in_=self, row=1, column=0)
        # поля ввода для директорий
        var_str_input_folder = tkinter.StringVar()
        var_str_output_folder = tkinter.StringVar()
        self.ent_inp_dir = ttk.Entry(self, width=40,
            textvariable=var_str_input_folder)
        self.ent_outp_dir = ttk.Entry(self, width=40,
            textvariable=var_str_output_folder)
        self.ent_inp_dir.grid(in_=self, row=0, column=1)
        self.ent_outp_dir.grid(in_=self, row=1, column=1)
        # кнопки для просмотра директории
        self.btn_brws_inp = ttk.Button(self, text="browse...")
        self.btn_brws_outp = ttk.Button(self, text="browse...")
        self.btn_brws_inp["command"] = \
            lambda : self.chose_directory(self.ent_inp_dir)
        self.btn_brws_outp["command"] = \
            lambda : self.chose_directory(self.ent_outp_dir)
        self.btn_brws_inp.grid(in_=self, row=0, column=2)
        self.btn_brws_outp.grid(in_=self, row=1, column=2)
        # self.ent_inp_dir.pack(in_=self)
        # self.ent_outp_dir.pack(in_=self)
        self.button_sort = ttk.Button(self, text="sort")
        self.button_sort.grid(in_=self, row=3, column=3)
        # self.button_sort.pack(in_=self)

    def chose_directory(self, entry):
        directory = filedialog.askdirectory()
        if os.path.isdir(directory):
            entry.delete(0, tkinter.END)
            entry.insert(0, directory)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(400, 400)
    sf = SortingFrame(root)
    sf.pack(in_=root)
    root.mainloop()