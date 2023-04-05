import tkinter as tk
janela=tk.Tk()

def inserir_texto(a):
    texto.insert(1.0,a)

texto=tk.Text(janela,height=2, width=16,font=("Arial", 25))
texto.grid(columnspan=4)

butao1=tk.Button(janela, text="1", width=5, height=3, font=("Arial", 15), command=lambda:inserir_texto("1"))
butao1.grid(column=1, row=2, )

janela.geometry("300x500")
janela.mainloop()