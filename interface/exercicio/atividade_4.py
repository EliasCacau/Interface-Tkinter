import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Soma Simples")
        self.janela.geometry("400x200")
        self.janela.configure(background="#333533")
        self.janela.resizable(0, 0)

        self.lbl1 = tk.Label(self.janela, text="Número 1:", bg="#f5cb5c", fg="#333533", font="Verdana")
        self.lbl1.grid(column=0, row=0, pady=2)
        self.ent1 = tk.Entry(self.janela, font="Verdana, 8", bg="#f5cb5c", fg="#333533", width=17)
        self.ent1.grid(column=1, row=0, pady=20, sticky=tk.S)

        self.lbl2 = tk.Label(self.janela, text="Número 2:", bg="#f5cb5c", fg="#333533", font="Verdana")
        self.lbl2.grid(column=0, row=1)
        self.ent2 = tk.Entry(self.janela, font="Verdana, 8", bg="#f5cb5c", fg="#333533", width=17)
        self.ent2.grid(column=1, row=1)

        self.lbl3 = tk.Label(self.janela, bg="#f5cb5c", width=17, height=2)
        self.lbl3.grid(column=1, row=2)
        def somar():
            soma = float(self.ent1.get()) + float(self.ent2.get())
            self.lbl4 = tk.Label(self.janela, text=f"{soma:2}", font="Verdana, 8", bg="#f5cb5c", fg="#333533", width=17, height=2)
            self.lbl4.grid(column=1, row=2)

        self.but = tk.Button(self.janela, text="Somar>>", command=somar, bg="#f5cb5c", fg="#333533", font="Verdana")
        self.but.grid(column=0, row=2)



janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()