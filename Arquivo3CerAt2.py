import tkinter as tk
from tkinter import messagebox
import random

def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif (
        (jogador == "Pedra" and computador == "Tesoura") or
        (jogador == "Papel" and computador == "Pedra") or
        (jogador == "Tesoura" and computador == "Papel")
        ):return "Jogador"
    else:
        return "Computador"


            #Não era possível escolher uma opção
def jogada_jogador(opcao):   

    opcoes = ["Pedra", "Papel", "Tesoura"]   #não havia uma definção para "opcoes"
    computador = random.choice(opcoes)  
    vencedor = verificar_vencedor(opcao, computador)


    resultado = f"Jogador escolheu: {opcao}\nComputador escolheu: {computador}\nVencedor: {vencedor}"

    messagebox.showinfo("Resultado", resultado)

def criar_interface():
    janela = tk.Tk()
    janela.title("Pedra, Papel, Tesoura")

    frame = tk.Frame(janela)
    frame.pack(pady=20)

    label_instrucao = tk.Label(frame, text="Escolha uma opção:")
    label_instrucao.pack()

    opcoes = ["Pedra", "Papel", "Tesoura"]

    for opcao in opcoes:
        botao = tk.Button(frame, text=opcao, width=10, command=lambda o=opcao: jogada_jogador(o))
        botao.pack(pady=5)

    janela.mainloop()

criar_interface()
