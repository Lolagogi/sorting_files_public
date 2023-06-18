import tkinter
from tkinter import ttk


class FrameSortingRules(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    def on_frame_configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        # Какое-то очень важное действие
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == '__main__':
    root = tkinter.Tk()
    root.minsize(200, 300)
    frm_srt_rls = FrameSortingRules(root)
    frm_srt_rls.pack(fill="both")
    pass