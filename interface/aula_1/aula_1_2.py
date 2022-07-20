import tkinter as tk

janela = tk.Tk()  # instância da classe TK
janela.title("First Window")  # Título
janela.minsize(300, 100)  # Tamanho mínimo da interface
janela.geometry("800x600")  # Tamanho da interface
container = tk.Frame(janela)  # Ajusta o tamanho do container
container.pack()  # Ajusta o tamanho do container

janela.mainloop()  # Método de execução da interface