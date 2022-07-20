import tkinter as tk

janela = tk.Tk()
janela.geometry('330x130')

lbl1 = tk.Label(janela, text='Pain', bg='#00fefe')
lbl1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lbl2 = tk.Label(janela, text='Dor', bg='#00ff00')
lbl2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#lbl2 = tk.Label(janela, text='RIGHT', bg='red')
#lbl2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


janela.mainloop()