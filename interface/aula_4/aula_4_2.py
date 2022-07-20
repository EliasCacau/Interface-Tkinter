import tkinter as tk

janela = tk.Tk()
janela.geometry('330x130')

lbl1 = tk.Label(janela, text='LEFT', bg='blue', fg='white')
lbl1.pack(side=tk.LEFT, fill=tk.X)

lbl2 = tk.Label(janela, text='RIGHT', bg='red')
lbl2.pack(side=tk.RIGHT, fill=tk.Y)

lbl3 = tk.Label(janela, text='TOP', bg='green')
lbl3.pack(side=tk.TOP, fill=tk.X)

lbl4 = tk.Label(janela, text='BOTTOM', bg='purple')
lbl4.pack(side=tk.BOTTOM, fill=tk.X)


janela.mainloop()