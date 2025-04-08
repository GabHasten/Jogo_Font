import tkinter as tk
from utilitarios import resetaTela,rodape

class TelaJogo:
    def __init__ (self,root):
        self.root = root

    def frameTelaJogo(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Pontuação: ").grid(row=0,column=0,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=1, padx=10)

        tk.Label(cabecalho, text="Partida: ").grid(row=0,column=2,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=3, padx=10)

        tk.Label(cabecalho, text="Tempo: ").grid(row=0,column=4,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=5, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial",10), command=lambda:self.pararJogo(root))
        botao_parar.grid(row=0,column=6,padx=10)

        numeros_frame = tk.Frame(self.root)
        numeros_frame.pack(pady=40)

        
        tk.Label(numeros_frame, text="1", font=("Arial",32)).pack(side="left",padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial",32)).pack(side="left",padx=20)
        tk.Label(numeros_frame, text="3", font=("Arial",32)).pack(side="left",padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial",32)).pack(side="left",padx=20)
        tk.Label(numeros_frame, text="4", font=("Arial",32)).pack(side="left",padx=20)

        operacoes_frame = tk.Frame(self.root)
        operacoes_frame.pack(pady=30)

        for operacao in["+","-","X","÷"]:
            tk.Button(operacoes_frame, text=operacao, font=("Arial",16), width=5,height=2).pack(side="left",padx=10)

        rodape(self.root)


    def pararJogo(self,root):
        root.running = False
        root.continua_jogo.set(True)
