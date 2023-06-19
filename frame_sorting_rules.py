import tkinter
from tkinter import ttk

from frame_sorting_rule import FrameSortingRule


class FrameSortingRules(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frms_sorting_rules = []
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tkinter.Canvas(self)
        self.frame = tkinter.Frame(self.canvas)
        self.sb = tkinter.Scrollbar(self,
            orient="vertical", command=self.canvas.yview)
        self.canvas["yscrollcommand"] = self.sb.set
        self.sb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window(
            (4, 4), window=self.frame, anchor="nw", tags="self.frame")
        # Привязываем событие - срабатывает при изменении параметров
        # "холста" (то же не знаю что делает)
        self.frame.bind("<Configure>", self.on_frame_configure)
        # виджеты для отображения столбцов
        # self.lbl_row_dirname = ttk.Label(self.frame, text="dirname")
        # self.lbl_row_extensions = ttk.Label(self.frame, text="extensions")
        # # self.lbl_row_dirname.grid(in_=self.frame, sticky="nsew")
        # # self.lbl_row_extensions.grid(in_=self.frame, sticky="nsew")
        # first_row = (self.lbl_row_dirname, self.lbl_row_extensions)
        # for column, widget in enumerate(first_row):
        #     widget.grid(in_=self.frame, row=1, column=column, sticky="nsew")

    def on_frame_configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        # Какое-то очень важное действие
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_sorting_rule(self):
        frm_srt_rl = FrameSortingRule(master=self, 
            del_func=lambda : self.del_sorting_rule(frm_srt_rl))
        frm_srt_rl.pack(in_=self.frame)
        self.frms_sorting_rules.append(frm_srt_rl)

    def del_sorting_rule(self, frm_srt_rl):
        frm_srt_rl.pack_forget()
        self.frms_sorting_rules.remove(frm_srt_rl)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(200, 300)
    frm_srt_rls = FrameSortingRules(root)
    frm_srt_rls.pack(fill="both")
    # for i in range(20):
    #     btn_1 = ttk.Button(frm_srt_rls, text="btn_1")
    #     btn_1.pack(in_=frm_srt_rls.frame)
    pass