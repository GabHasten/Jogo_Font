import tkinter as tk
from utilitarios import resetaTela, rodape
from tela_jogo import TelaJogo
from logica_jogo import DadosOperacionais



class TelaInstrucoes:
    def __init__(self,root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        titulo = tk.Label(self.root, text="Instruções", font=("Arial",24,"bold"),bg="#262626",fg="#D99748")
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root, 
            text="Clique na operação que corresponde ao resultados entre os dois números\nAs operações são |x| |÷| |-| |+|",
            font=("Arial",11,"bold"),
            bg="#262626",
            fg="#F2EEB6"
            )

        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar",
            command=self.abrirTelajogo,
            font=("Arial",16),
            width=10,
            height=2,
            bg="#262626",
            fg="#D99748"
        )
        
        botao_play.pack(pady=20)

        rodape(self.root)
        

    def abrirTelajogo(self):
        tela_jogo = TelaJogo(self.root)
        DadosOperacionais.iniciaJogo(tela_jogo,self.root)