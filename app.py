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
        self.entry_input_folder = ttk.Entry(self, width=40,
            textvariable=var_str_input_folder)
        self.entry_output_folder = ttk.Entry(self, width=40,
            textvariable=var_str_output_folder)
        self.entry_input_folder.grid(in_=self, row=0, column=1)
        self.entry_output_folder.grid(in_=self, row=1, column=1)
        # кнопки для просмотра директории
        self.button_browse_input = ttk.Button(self, text="browse...")
        self.button_browse_output = ttk.Button(self, text="browse...")
        self.button_browse_input.entry = self.entry_input_folder
        self.button_browse_output.entry = self.entry_output_folder
        self.button_browse_input.bind("<1>", self.chose_folder)
        self.button_browse_output.bind("<1>", self.chose_folder)
        self.button_browse_input.grid(in_=self, row=0, column=2)
        self.button_browse_output.grid(in_=self, row=1, column=2)
        # self.entry_input_folder.pack(in_=self)
        # self.entry_output_folder.pack(in_=self)
        self.button_sort = ttk.Button(self, text="sort")
        self.button_sort.grid(in_=self, row=3, column=3)
        # self.button_sort.pack(in_=self)

    def chose_folder(self, event):
        widget = event.widget
        entry = widget.entry
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