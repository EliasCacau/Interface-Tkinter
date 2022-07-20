import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Third Window")
        self.janela.minsize(300,100)
        self.janela.maxsize(1280,720)
        self.janela.geometry("800x600")
        self.container = tk.Frame(self.janela)
        self.container.pack()


janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()