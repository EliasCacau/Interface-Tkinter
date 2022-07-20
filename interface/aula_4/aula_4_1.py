import tkinter as tk


class Place:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Place")
        self.janela.minsize(300, 100)
        self.janela.geometry("330x130")
        self.lbl1 = tk.Label(self.janela, text="x=10, y=10", bg="blue")
        self.lbl1.place(x=10, y=10)

        self.lbl2 = tk.Label(self.janela, text="x=60, y=35", bg="orange")
        self.lbl2.place(x=60, y=35)

        self.lbl3 = tk.Label(self.janela, text="x=140, y=60", bg="yellow")
        self.lbl3.place(x=140, y=60)

        self.lbl4 = tk.Label(self.janela, text="relx=.5, rely=.9", bg="black", fg="white")
        self.lbl4.place(relx=.5, rely=.9, anchor='center')

janelaPrincipal = tk.Tk()
Place(janelaPrincipal)
janelaPrincipal.mainloop()
