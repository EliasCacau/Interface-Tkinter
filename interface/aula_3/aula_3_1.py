import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("ComboBox")
        # self.janela.minsize(244, 120)
        # self.janela.maxsize(1280, 720)
        self.janela.geometry("800x600")
        self.janela.resizable(width=False, height=False)
        self.janela.configure(background="#20b2aa")
        self.v = tk.StringVar()
        self.cbx = ttk.Combobox(self.janela, textvariable=self.v, width=12)
        self.cbx['values'] = ('Domingo', 'Segunda', 'Terça')
        self.cbx.current(1)
        self.cbx.pack()


app = tk.Tk()
Tela(app)
app.mainloop()
