import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Gerenciador Grid")
        self.janela.geometry("200x180")
        self.janela.resizable(0, 0)
        self.but1 = tk.Button(self.janela, text='1', width="5", height="2")
        self.but1.grid(column=1, row=0,   padx=0, pady=0)

        self.but2 = tk.Button(self.janela, text='2', width="5", height="2")
        self.but2.grid(column=0, row=1, padx=0, columnspan=2)

        self.but3 = tk.Button(self.janela, text='3', width="5", height="2")
        self.but3.grid(column=1, row=1, padx=0, pady=0, columnspan=2)

        self.but4 = tk.Button(self.janela, text='4', width="5", height="2")
        self.but4.grid(column=0, row=2, padx=0, pady=0)

        self.but5 = tk.Button(self.janela, text='5', width="5", height="2")
        self.but5.grid(column=1, row=2, padx=0, pady=0)

        self.but6 = tk.Button(self.janela, text='6', width="5", height="2")
        self.but6.grid(column=2, row=2, padx=0, pady=0)


janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()