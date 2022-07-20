import tkinter as tk


class CheckButton:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo CheckButton")
        self.janela.minsize(244, 120)
        self.janela.maxsize(1280, 720)
        self.janela.geometry('800x600')

        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()

        self.ckb = tk.Checkbutton(self.janela, text='Opção 1', variable=self.v1).pack()
        self.ckb = tk.Checkbutton(self.janela, text='Opção 1', variable=self.v2).pack()

janelaPrincipal = tk.Tk()
CheckButton(janelaPrincipal)
janelaPrincipal.mainloop()