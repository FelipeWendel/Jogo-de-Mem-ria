import tkinter as tk
import random

class JogoDeMemoria:
    def __init__(self):
        self.cores = ['vermelho', 'azul', 'amarelo', 'verde', 'roxo']
        self.sequencia = []
        self.usuario_sequencia = []
        self.pontos = 0

        self.janela = tk.Tk()
        self.janela.title("Jogo de Memória")

        self.label = tk.Label(self.janela, text="Lembre-se da sequência de cores!")
        self.label.pack()

        self.botao_vermelho = tk.Button(self.janela, bg="red", command=lambda: self.usuario_escolhe("vermelho"))
        self.botao_vermelho.pack(side=tk.LEFT)

        self.botao_azul = tk.Button(self.janela, bg="blue", command=lambda: self.usuario_escolhe("azul"))
        self.botao_azul.pack(side=tk.LEFT)

        self.botao_amarelo = tk.Button(self.janela, bg="yellow", command=lambda: self.usuario_escolhe("amarelo"))
        self.botao_amarelo.pack(side=tk.LEFT)

        self.botao_verde = tk.Button(self.janela, bg="green", command=lambda: self.usuario_escolhe("verde"))
        self.botao_verde.pack(side=tk.LEFT)

        self.botao_roxo = tk.Button(self.janela, bg="purple", command=lambda: self.usuario_escolhe("roxo"))
        self.botao_roxo.pack(side=tk.LEFT)

        self.gerar_sequencia()

    def gerar_sequencia(self):
        self.sequencia.append(random.choice(self.cores))
        self.label['text'] = "Lembre-se da sequência de cores!"
        self.janela.update()
        self.janela.after(1000, self.mostrar_sequencia)

    def mostrar_sequencia(self):
        for cor in self.sequencia:
            self.label['text'] = cor
            self.janela.update()
            self.janela.after(500)

        self.label['text'] = "Sua vez!"
        self.usuario_sequencia = []

    def usuario_escolhe(self, cor):
        self.usuario_sequencia.append(cor)
        if self.usuario_sequencia == self.sequencia:
            self.pontos += 1
            self.label['text'] = "Acertou! Pontos: " + str(self.pontos)
            self.gerar_sequencia()
        elif self.usuario_sequencia != self.sequencia[:len(self.usuario_sequencia)]:
            self.label['text'] = "Errou! Pontos: " + str(self.pontos)
            self.janela.after(2000, self.gerar_sequencia)

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    jogo = JogoDeMemoria()
    jogo.run()