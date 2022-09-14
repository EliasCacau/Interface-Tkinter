import sqlite3
from sqlite3 import Error

def conexao_banco():
    caminho = "/home/joao.sa/banco.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

def inserir(insert):
    con = conexao_banco()
    cursor = con.cursor()
    cursor.execute(insert)
    #cursor.execute(delete)
    con.commit()
    con.close()
    print("Dados inseridos no Banco com Sucesso!")
def update(update):
    con = conexao_banco()
    cursor = con.cursor()
    cursor.execute(update)
    con.commit()
    con.close()
    print("Dados atualizados no Banco com Sucesso!")
def delete(delete):
    con = conexao_banco()
    cursor = con.cursor()
    cursor.execute(delete)
    con.commit()
    con.close()
    print("Dados deletados do Banco com Sucesso!")
def consultar(consultar):
    con = conexao_banco()
    cursor = con.cursor()
    cursor.execute(consultar)
    valores = cursor.fetchall()
    for i in valores:
        print(i[0], i[1], i[2])
    con.close()
valor = ''

while valor != "n":
    # sql_tabela = 'CREATE TABLE cliente(id INTERGER AUTO_INCRIMENT PRIMARY KEY, nome VARCHAR(60) NOT NULL, cpf VARCHAR(11) NOT NULL);'
    operacao = input("Que operação deseja fazer?\n1 - inserir\n2 - atualizar\n3 - deletar\n4 - mostrar\n")
    sql_consultar = 'SELECT * FROM cliente'
    if operacao == "1":
        consultar(sql_consultar)
        id = input("Id: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        sql_insert = f"INSERT INTO cliente VALUES({id}, '{nome}', '{cpf}');"
        inserir(sql_insert)
    elif operacao == "2":
        consultar(sql_consultar)
        op = input("O que deseja atualizar?\n1 - nome\n2 - CPF\n")
        if op == "1":
            id = input("Id: ")
            nome = input("Nome: ")
            sql_update = f"UPDATE cliente SET nome='{nome}' WHERE id={id};"
        else:
            id = input("Id: ")
            cpf = input("CPF: ")
            sql_update = f"UPDATE cliente SET cpf='{cpf}' WHERE id={id};"
        update(sql_update)
    elif operacao == "3":
        consultar(sql_consultar)
        id = input("Id: ")
        sql_delete = f"DELETE FROM CLIENTE WHERE id={id};"
        delete(sql_delete)
    else:
        consultar(sql_consultar)

    valor = input('Deseja continuar?\n"s" para continuar "n" para fechar:\n')


