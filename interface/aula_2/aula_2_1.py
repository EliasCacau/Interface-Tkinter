import tkinter as tk


class Label:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Label and Entry")
        self.janela.minsize(240, 120)
        self.janela.maxsize(1980, 1080)
        self.janela.geometry("800x600")
        # label e entry usuário
        self.lbl_nome = tk.Label(self.janela, text="Nome:", font=('calibre', 10, 'bold')).pack()
        self.etr_nome = tk.Entry(self.janela, width=20, bg='black', fg='white').pack()

        self.lbl_senha = tk.Label(self.janela, text='Senha:', font=('calibre', 10, 'bold')).pack()
        self.etr_senha = tk.Entry(self.janela, width=20, show=('*'), bg='black', fg='white').pack()

        self.btn_logar = tk.Button(self.janela, text="Logar", command=self.janela.destroy).pack()

janelaPrincipal = tk.Tk()
Label(janelaPrincipal)
janelaPrincipal.mainloop()
