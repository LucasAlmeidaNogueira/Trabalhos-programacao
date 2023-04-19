import tkinter as tk
janela=tk.Tk()
calculo=str()

def inserir_texto(a):
    
    global calculo
    texto.delete(1.0,"end")
    
    calculo=calculo+a
    texto.insert(1.0,calculo)

def apagar_tudo():

    global calculo
    calculo=str()
    texto.delete(1.0, "end")


def calcular():

    global calculo
    x=str(eval(texto.get(1.0, "end")))
    
    calculo=str()
    inserir_texto(x)
    

texto=tk.Text(janela,height=2, width=23,font=("Arial", 25))
texto.grid(columnspan=5)


butao1=tk.Button(janela, text="1", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("1"))
butao1.grid(column=1, row=1, )
butao2=tk.Button(janela, text="2", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("2"))
butao2.grid(column=2, row=1, )
butao3=tk.Button(janela, text="3", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("3"))
butao3.grid(column=3, row=1, )
butao4=tk.Button(janela, text="4", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("4"))
butao4.grid(column=1, row=2, )
butao5=tk.Button(janela, text="5", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("5"))
butao5.grid(column=2, row=2, )
butao6=tk.Button(janela, text="6", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("6"))
butao6.grid(column=3, row=2, )
butao7=tk.Button(janela, text="7", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("7"))
butao7.grid(column=1, row=3, )
butao8=tk.Button(janela, text="8", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("8"))
butao8.grid(column=2, row=3, )
butao9=tk.Button(janela, text="9", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("9"))
butao9.grid(column=3, row=3, )
butao0=tk.Button(janela, text="0", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("0"))
butao0.grid(column=2, row=4, )
butaoAParenteses=tk.Button(janela, text="(", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto("("))
butaoAParenteses.grid(column=1, row=4, )
butaoFParenteses=tk.Button(janela, text=")", width=8, height=3, font=("Arial", 15), command=lambda:inserir_texto(")"))
butaoFParenteses.grid(column=3, row=4, )


butaoIgual=tk.Button(janela, text="=", width=17, height=3, font=("Arial", 15), command=lambda:calcular())
butaoIgual.grid(column=1, row=5, columnspan=2 )
butaoMais=tk.Button(janela, text="+", width=11, height=3, font=("Arial", 15), command=lambda:inserir_texto("+"))
butaoMais.grid(column=4, row=2, )
butaoMenos=tk.Button(janela, text="-", width=11, height=3, font=("Arial", 15), command=lambda:inserir_texto("-"))
butaoMenos.grid(column=4, row=3, )
butaoVezes=tk.Button(janela, text="X", width=11, height=3, font=("Arial", 15), command=lambda:inserir_texto("*"))
butaoVezes.grid(column=4, row=4, )
butaoDivisao=tk.Button(janela, text="/", width=11, height=3, font=("Arial", 15), command=lambda:inserir_texto("/"))
butaoDivisao.grid(column=4, row=5, )
butaoCezinho=tk.Button(janela, text="C", width=8, height=3, font=("Arial", 15), command=lambda:apagar_tudo())
butaoCezinho.grid(column=3, row=5, )
butaoElevado=tk.Button(janela, text="^", width=11, height=3, font=("Arial", 15), command=lambda:inserir_texto("**"))
butaoElevado.grid(column=4, row=1, )




janela.geometry("425x510")
janela.mainloop()
