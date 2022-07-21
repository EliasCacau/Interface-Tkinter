import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Soma Simples")
        self.janela.geometry("250x130")
        self.janela.resizable(0, 0)
        self.lbl1 = tk.Label(self.janela, text="Número 1:")
        self.lbl1.grid(column=0, row=0, stick=tk.EW, padx=1, pady=5)
        self.ent1 = tk.Entry(self.janela, width=15)
        self.ent1.grid(column=1, row=0)
        self.lbl2 = tk.Label(self.janela, text="Número 2:")
        self.lbl2.grid(column=0, row=1, stick=tk.EW, padx=1, pady=5)
        self.ent2 = tk.Entry(self.janela, width=15)
        self.ent2.grid(column=1, row=1)
        self.lbl3 = tk.Label(self.janela, width=14, bg="white", height=1)
        self.lbl3.grid(column=1, row=2, stick=tk.EW, padx=5)
        def somar():
            soma = float(self.ent1.get()) + float(self.ent2.get())
            self.lbl4 = tk.Label(self.janela, text=f"{soma:.1f}", bg="white", width=14)
            self.lbl4.grid(column=1, row=2)
        self.but = tk.Button(self.janela, text="Somar >>", command=somar, width=10)
        self.but.grid(column=0, row=2, stick=tk.EW, pady=5)



janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()