import tkinter as tk


class RadiosButton:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo RadioButton")
        self.janela.minsize(244, 120)
        self.janela.maxsize(1280, 720)

        self.rbt_1 = tk.Radiobutton(self.janela, text='Opção 1', value=1).pack()
        self.rbt_2 = tk.Radiobutton(self.janela, text='Opção 2', value=2).pack()
        self.rbt_3 = tk.Radiobutton(self.janela, text='Opção 3', value=3).pack()

janelaPrincipal = tk.Tk()
RadiosButton(janelaPrincipal)
janelaPrincipal.mainloop()