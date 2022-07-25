import tkinter as tk
from tkinter import RAISED, RIDGE
from tkinter import ttk

class CombosLogin:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Combos Login")
        self.janela.geometry("800x600")
        self.janela.configure(bg="#002d4a")

        self.tit = tk.Label(self.janela, text="Login", font="verdana, 24", bg="#002d4a", fg="white")
        self.tit.grid(column=1, row=0, padx=280, pady=10, sticky=tk.N)

        self.usuario = tk.Label(self.janela, text="Usuário:", font="verdana, 16", bg="#002d4a", fg="white")
        self.usuario.grid(column=0, row=1, pady=7)
        self.ent_log = tk.Entry(self.janela, bg="#00a8fc", font="verdana, 16")
        self.ent_log.grid(column=1, row=1, sticky=tk.W, padx=5)

        self.senha = tk.Label(self.janela, text="Senha:", font="verdana, 16", bg="#002d4a", fg="white")
        self.senha.grid(column=0, row=2, sticky=tk.NW)
        self.ent_sen = tk.Entry(self.janela, bg="#00a8fc", show="*", font="verdana, 16")
        self.ent_sen.grid(column=1, row=2, sticky=tk.W, padx=5)

        self.but = tk.Button(self.janela, text="Logar", font="verdana, 16", bg="#00669c", fg="white", width=12, relief=RAISED, overrelief=RIDGE)
        self.but.grid(column=1, row=3, sticky=tk.W, pady=15, padx=50)

        self.menu_barra = tk.Menu(self.janela)
        self.menu_arquivo = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_arquivo.add_command(label="Novo", command=None)
        self.menu_arquivo.add_command(label="Editar", command=None)
        self.menu_arquivo.add_command(label="Sair", command=self.janela.destroy)

        self.menu_salvar = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Salvar", menu=self.menu_salvar)
        self.menu_salvar.add_command(label="Salvou o dia", command=None)
        self.menu_salvar.add_command(label="Salvou a noite", command=None)
        self.janela.configure(menu=self.menu_barra)

        self.scrollbar = tk.Scrollbar(self.janela)
        self.scrollbar.grid(column=0, row=4, rowspan=5, sticky=tk.NS)

        self.lbl1 = tk.Label(self.janela, text="Deixe seu comentário:", font="verdana, 16", bg="#002d4a", fg="white")
        self.lbl1.grid(column=0, row=4, columnspan=5, sticky=tk.W)

        self.text = tk.Text(self.janela, width=50, height=10, font="verdana, 12")
        self.text.grid(column=0, row=5, columnspan=10, sticky=tk.W)

        # RADIOBUTTON
        # self.valor = tk.StringVar(self.janela)
        # self.dic = {"Opção 1" : "1", "Opção 2" : "2", "Opção 3" : "3", "Opção 4" : "4"}
        # x = 6
        # for (texto, op) in self.dic.items():
        #     tk.Radiobutton(self.janela, text=texto, variable=self.valor, value=op).grid(column=0, row=x)
        #     x += 1

        self.rbt1 = tk.Radiobutton(self.janela, text="Opção 1", value=1)
        self.rbt1.grid(column=0, row=6)
        self.rbt2 = tk.Radiobutton(self.janela, text="Opção 2", value=2)
        self.rbt2.grid(column=0, row=7)
        self.rbt3 = tk.Radiobutton(self.janela, text="Opção 3", value=3)
        self.rbt3.grid(column=0, row=8)

        self.valor1 = tk.IntVar()
        self.valor2 = tk.IntVar()

        self.bc1 = tk.Checkbutton(self.janela, text="Checa 1", variable=self.valor1)
        self.bc1.grid(column=1, row=6, columnspan=2)

        self.bc2 = tk.Checkbutton(self.janela, text="Checa 2", variable=self.valor2)
        self.bc2.grid(column=1, row=7, columnspan=2)

        self.cbx = ttk.Combobox(width=12)
        self.cbx['values'] = ('Elias', 'Gostoso', 'DanoneELIAS')
        self.cbx.current(1)
        self.cbx.grid(column=0, row=10)

app = tk.Tk()
CombosLogin(app)
app.mainloop()