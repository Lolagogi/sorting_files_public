import tkinter
from tkinter import ttk


class FrameSortingRule(ttk.Frame):

    def __init__(self, del_func=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.del_func = del_func
        self.create_widgets()

    def create_widgets(self):
        self.lbl_frm_folder_name = ttk.LabelFrame(self, text="dirname")
        self.lbl_frm_extensions = ttk.LabelFrame(self, text="extensions")
        self.lbl_frm_folder_name.grid(in_=self, row=0, column=0)
        self.lbl_frm_extensions.grid(in_=self, row=0, column=1)
        self.ent_folder_name = ttk.Entry(self.lbl_frm_folder_name)
        self.ent_extensions = ttk.Entry(self.lbl_frm_extensions)
        self.ent_folder_name.pack()
        self.ent_extensions.pack()
        self.btn_del = ttk.Button(self, text="X", width=5)
        if callable(self.del_func):
            self.btn_del["command"] = self.del_func
        self.btn_del.grid(in_=self, row=0, column=2, sticky="nsew")

    def get_sorting_rule(self):
        dir_n_extens = {}
        dir_n_extens["dirname"] = self.ent_folder_name.get()
        dir_n_extens["extensions"] = self.ent_extensions.get()
        if all(dir_n_extens.values()): 
            return dir_n_extens

if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(200, 300)
    # sr = SimpleSortingRule("pictures", ["jpg", "jpeg"])
    frm_srt_rl = FrameSortingRule(root)
    frm_srt_rl.pack(in_=root, fill="both")
    frm_srt_rl.bind("<Return>", lambda e: print(frm_srt_rl.get_sorting_rule()))
