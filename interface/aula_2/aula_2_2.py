import tkinter as tk

class Button:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Insert Button")
        self.janela.minsize(244, 120)
        self.janela.maxsize(1280, 720)
        self.janela.geometry('800x600')
        self.lbl_nome = tk.Label(self.janela, text="Nome:", font=('calibre', 10, 'bold')).pack()
        self.ent_nome = tk.Entry(self.janela, width=20, bg="black", fg="white").pack()

        self.lbl_senha = tk.Label(self.janela, text="Senha", font=('calibre', 10, 'bold')).pack()
        self.ent_senha = tk.Entry(self.janela, width=20, bg="black", fg="white").pack()

        self.btn_logar = tk.Button(self.janela, text="Logar", command=self.janela.destroy, activebackground="red", bg="grey", fg="white").pack()

janelaPrincipal = tk.Tk()
Button(janelaPrincipal)
janelaPrincipal.mainloop()