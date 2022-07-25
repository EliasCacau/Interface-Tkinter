import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Soma Simples")
        self.janela.geometry("250x130")
        self.janela.configure(background="#333533")
        self.janela.resizable(0, 0)

        self.lbl1 = tk.Label(self.janela, text="Número 1:", bg="#f5cb5c", fg="#333533", font="Verdana", anchor=tk.CENTER)
        self.lbl1.grid(column=0, row=0, stick=tk.EW, padx=1, pady=5)
        self.ent1 = tk.Entry(self.janela, font="Verdana, 12", bg="#f5cb5c", fg="#333533", width=15)
        self.ent1.grid(column=1, row=0)

        self.lbl2 = tk.Label(self.janela, text="Número 2:", bg="#f5cb5c", fg="#333533", font="Verdana")
        self.lbl2.grid(column=0, row=1, stick=tk.EW, padx=1, pady=5)
        self.ent2 = tk.Entry(self.janela, font="Verdana, 12", bg="#f5cb5c", fg="#333533", width=15)
        self.ent2.grid(column=1, row=1)

        self.lbl3 = tk.Label(self.janela, bg="orange", width=14, height=2)
        self.lbl3.grid(column=1, row=2, stick=tk.EW)
        def somar():
            soma = float(self.ent1.get()) + float(self.ent2.get())
            self.lbl4 = tk.Label(self.janela, text=f"{soma:.1f}", font="Verdana, 12", bg="orange", fg="#333533", width=14)
            self.lbl4.grid(column=1, row=2)

        self.but = tk.Button(self.janela, text="Somar >>", command=somar, bg="#f5cb5c", fg="#333533", font="Verdana, 12", width=10)
        self.but.grid(column=0, row=2, stick=tk.EW, pady=5)



janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()