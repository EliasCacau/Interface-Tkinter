import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Third Window")
        self.janela.minsize(300, 100)
        self.janela.maxsize(1280, 720)
        self.janela.geometry("800x600")
        self.container = tk.Frame(self.janela)
        self.container.pack()
        self.lbl = tk.Label(self.janela, text="First Text", bg="#000000", foreground="white")
        self.lbl.config(font=("Verdana", "72"))
        self.lbl.pack()


janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()