import tkinter 
from tkinter import ttk


class SortingFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label_input = ttk.Label(self, text="input directory")
        self.label_output = ttk.Label(self, text="output directory")
        self.label_input.grid(in_=self, row=0, column=0)
        self.label_output.grid(in_=self, row=1, column=0)
        var_str_input_folder = tkinter.StringVar()
        var_str_output_folder = tkinter.StringVar()
        self.entry_input_folder = ttk.Entry(self, text="OK",
            textvariable=var_str_input_folder)
        self.entry_output_folder = ttk.Entry(self, 
            textvariable=var_str_output_folder)
        self.entry_input_folder.grid(in_=self, row=0, column=1)
        self.entry_output_folder.grid(in_=self, row=1, column=1)
        # self.entry_input_folder.pack(in_=self)
        # self.entry_output_folder.pack(in_=self)
        self.button_sort = ttk.Button(self, text="sort")
        self.button_sort.grid(in_=self, row=3, column=3)
        # self.button_sort.pack(in_=self)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(400, 400)
    sf = SortingFrame(root)
    sf.pack(in_=root)
    root.mainloop()