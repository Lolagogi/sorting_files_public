import tkinter
from tkinter import ttk

from sorting_rule import SimpleSortingRule


class FrameSortingRule(ttk.Frame):

    def __init__(self, sorting_rule, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sorting_rule = sorting_rule
        self.create_widgets()
        self.update_widgets()

    def create_widgets(self):
        self.lbl_folder_name = ttk.Label(self)
        self.lbl_extensions = ttk.Label(self)
        self.lbl_folder_name.grid(in_=self, row=0, column=0)
        self.lbl_extensions.grid(in_=self, row=0, column=1)

    def update_widgets(self):
        self.lbl_folder_name["text"] = self.sorting_rule.dirname
        self.lbl_extensions["text"] = ", ".join(self.sorting_rule.extensions)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(200, 300)
    sr = SimpleSortingRule("pictures", ["jpg", "jpeg"])
    frm_srt_rls = FrameSortingRule(master=root, sorting_rule=sr)
    frm_srt_rls.pack(fill="both")
    pass