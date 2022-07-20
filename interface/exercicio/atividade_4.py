import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Soma Simples")
        self.janela.geometry("400x200")
        self.janela.configure(background='grey')
        self.janela.resizable(0, 0)
        self.lbl1 = tk.Label(self.janela, text="Número 1:")
        self.lbl1.grid(column=0, row=0)
        self.ent1 = tk.Entry(self.janela)
        self.ent1.grid(column=1, row=0)

        self.lbl2 = tk.Label(self.janela, text="Número 1:")
        self.lbl2.grid(column=0, row=1)
        self.ent2 = tk.Entry(self.janela)
        self.ent2.grid(column=1, row=1)

        def somar():
            soma = int(self.ent1.get()) + int(self.ent2.get())
            return soma

        self.but = tk.Button(self.janela, text="Somar>>", command=somar)
        self.but.grid(column=0, row=2)

        self.lbl3 = tk.Label(self.janela, text=somar())

janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()