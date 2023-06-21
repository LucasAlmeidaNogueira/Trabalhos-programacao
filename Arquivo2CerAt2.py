import tkinter as tk
import random
import time
from tkinter import messagebox #TIVE QUE ESCREVER ESSA LINHA PARA O CODIGO ENTENDER O COMANDO
def iniciar_simulador():
    tempo_espera = random.randint(1000, 5000)  # Gera um tempo aleatório de espera entre 1 e 5 segundos
    janela.after(tempo_espera, exibir_alvo)

def exibir_alvo():
    global tempo_inicio

    tempo_inicio = time.time()
    canvas.create_oval(50, 50, 150, 150, fill="red")  # Desenha um círculo vermelho (alvo) no canvas

def clicar_alvo(event):
    global tempo_inicio

    tempo_reacao = time.time() - tempo_inicio
    messagebox.showinfo("Resultado", f"Seu tempo de reação foi de {tempo_reacao:.3f} segundos.")

    canvas.delete("all")  # Limpa o canvas
    iniciar_simulador()

janela = tk.Tk()
janela.title("Simulador de Tempo de Reação")

canvas = tk.Canvas(janela, width=200, height=200)
canvas.pack(padx=20, pady=20)

canvas.bind("<Button-1>", clicar_alvo)

tempo_inicio = 0

iniciar_simulador()

janela.mainloop()
