import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Janela:
    def __init__(self, master):
        def conexao_banco():
            caminho = "/home/joao.sa/banco.db"
            con = None
            try:
                con = sqlite3.connect(caminho)
                return con
            except Error as error:
                messagebox.showwarning("ERRO DE CONEXÃO")
                print(error)

        def inserir():
            print(self.ent_nome.get())
            dados = f"INSERT INTO cliente VALUES (NULL, '{self.ent_nome.get()}', '{self.ent_cpf.get()}');"
            con = conexao_banco()
            cursor = con.cursor()
            cursor.execute(dados)
            con.commit()
            valores = cursor.fetchall()
            for i in valores:
                if i[1] == self.ent_nome.get() and i[2] == self.ent_cpf.get():
                    self.tvw.insert("", tk.END, values=(i[0], i[1], i[2]))
            con.close()

        def update(update):
            con = conexao_banco()
            cursor = con.cursor()
            cursor.execute(update)
            con.commit()
            con.close()

        def delete(delete):
            con = conexao_banco()
            cursor = con.cursor()
            cursor.execute(delete)
            con.commit()
            con.close()

        def atualizar():
            sql_consultar = 'SELECT * FROM cliente'
            con = conexao_banco()
            cursor = con.cursor()
            cursor.execute(sql_consultar)
            valores = cursor.fetchall()
            con.close()
            for i in valores:
                self.tvw.insert("", tk.END, values=(i[0], i[1], i[2]))
            return valores

        self.janela = master
        self.janela.geometry("650x400")
        self.janela.title("Cadastro de clientes")
        self.frm_entradas = tk.Frame(self.janela)
        self.frm_entradas.pack()

        self.lbl_nome = tk.Label(self.frm_entradas, text="Nome:")
        self.lbl_nome.grid(column=0, row=0)
        self.ent_nome = tk.Entry(self.frm_entradas)
        self.ent_nome.grid(column=1, row=0)

        self.lbl_cpf = tk.Label(self.frm_entradas, text="CPF:")
        self.lbl_cpf.grid(column=0, row=1)
        self.ent_cpf = tk.Entry(self.frm_entradas)
        self.ent_cpf.grid(column=1, row=1)

        self.btn_inserir = tk.Button(self.frm_entradas, text="Inserir", command=inserir)
        self.btn_inserir.grid(column=1, row=2, columnspan=2)

        self.frm_tvw = tk.Frame(self.janela)
        self.frm_tvw.pack()
        colunas = ('id', 'nome', 'cpf')
        self.tvw = ttk.Treeview(self.frm_tvw, columns=colunas, show='headings')
        self.tvw.pack(side=tk.LEFT)

        self.tvw.heading('id', text='Id')  # cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('cpf', text='CPF')

        self.scr = ttk.Scrollbar(self.frm_tvw, command=self.tvw.yview)  # scrollbar
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

        valores = atualizar()
        for i in valores:
            self.tvw.insert("", tk.END, values=(i[0], i[1], i[2]))

        self.btn_renomear = tk.Button(self.janela, text="Renomar")
        self.btn_renomear.pack(side = tk.LEFT)
        self.btn_atualizar = tk.Button(self.janela, text="Atualizar", command=atualizar)
        self.btn_atualizar.pack(side = tk.LEFT)
        self.btn_fechar = tk.Button(self.janela, text="Fechar")
        self.btn_fechar.pack(side = tk.LEFT)


app = tk.Tk()
Janela(app)
app.mainloop()