import tkinter as tk
import time

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronômetro")
        
        self.tempo_inicial = 0
        self.tempo_pausado = 0
        self.cronometro_ativo = False
        
        self.label_cronometro = tk.Label(janela, text="00:00:00", font=("Arial", 24), padx=20, pady=10)
        self.label_cronometro.pack()
        
        self.botao_iniciar = tk.Button(janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack()
        
        self.botao_pausar = tk.Button(janela, text="Pausar", state=tk.DISABLED, command=self.pausar_cronometro)
        self.botao_pausar.pack()
        
        self.botao_parar = tk.Button(janela, text="Parar", state=tk.DISABLED, command=self.parar_cronometro)
        self.botao_parar.pack()
        
                                    #Cronometro não iniciava ao apertar no botão de iniciar
    def iniciar_cronometro(self):
        if not self.cronometro_ativo:
            self.tempo_inicial = time.time() - self.tempo_pausado
            self.atualizar_cronometro()
            self.cronometro_ativo = True
            self.botao_iniciar.config(state=tk.DISABLED)
            self.botao_pausar.config(state=tk.NORMAL)
            self.botao_parar.config(state=tk.NORMAL)
    
    def pausar_cronometro(self):
        if self.cronometro_ativo:
            self.tempo_pausado = time.time() - self.tempo_inicial
            self.cronometro_ativo = False
            self.botao_pausar.config(state=tk.DISABLED)
            self.botao_iniciar.config(state=tk.NORMAL)
    
    def parar_cronometro(self):
        if self.cronometro_ativo:
            self.cronometro_ativo = False
            self.botao_iniciar.config(state=tk.NORMAL)
            self.botao_pausar.config(state=tk.DISABLED)
            self.botao_parar.config(state=tk.DISABLED)
        self.tempo_pausado = 0
        self.label_cronometro.config(text="00:00:00")
    
    def atualizar_cronometro(self):
        if self.cronometro_ativo:
            tempo_decorrido = time.time() - self.tempo_inicial

            horas = int(tempo_decorrido // 3600)
            minutos = int((tempo_decorrido % 3600) // 60)
            segundos = int(tempo_decorrido % 60)

            self.label_cronometro.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
            self.janela.after(1000, self.atualizar_cronometro)

# Configuração da janela
janela = tk.Tk()

# Instanciar o cronômetro
cronometro = Cronometro(janela)

# Execução da janela
janela.mainloop()
