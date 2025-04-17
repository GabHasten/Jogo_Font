import tkinter as tk
import tkinter as tk
from utilitarios import resetaTela, rodape

class FimJogo():
    def __init__(self, root, pontos=0, acertos=0, partidas=0):
        self.root = root
        self.pontos = pontos
        self.acertos = acertos
        self.partidas = partidas

    def frameTelaFinal(self):
        resetaTela(self.root)
        self.root.running = False
        self.root.title("The Math Game")

        titulo = tk.Label(self.root, text="Fim do jogo!",bg="#262626",fg="#D99748", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text=f"Parabéns pela partida!\n"
            f"Você marcou {self.pontos} pontos e acertou {self.acertos} de {self.partidas} Questões!",
            font=("Arial", 14),bg="#262626",fg="#D99748"
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar Novamente",
            command=self.abrirTelaInstrucoes,
            font=("Arial", 16),
            width=15,
            bg="#262626",
            fg="#D99748",
            height=2
        )
        botao_play.pack(pady=10)

        botao_sair = tk.Button(
            self.root,
            text="Sair do Jogo",
            command=self.sairJogo,
            font=("Arial", 16),
            width=15,
            bg="#262626",
            fg="#D99748",
            height=2
        )
        botao_sair.pack(pady=10)

        rodape(self.root)

    def abrirTelaInstrucoes(self):
        from tela_instrucoes import TelaInstrucoes
        TelaInstrucoes(self.root).frameTelaInstrucoes()

    def sairJogo(self):
        self.root.running = False
        self.root.destroy()
