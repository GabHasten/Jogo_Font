import tkinter as tk
from utilitarios import resetaTela
from logica_jogo import DadosFuncionais

class TelaJogo:
    def __init__(self,root):
        self.root = root
        self.operador_correto = None
        self.num1 = None
        self.num2 = None
        self.resultado = None

    def frameTelaJogo(self, root, partida_atual, pontos):  
        resetaTela(root)
        self.root.title("The Math Game")

        self.num1, self.num2 = DadosFuncionais.gerarNumeros()
        self.operador_correto = DadosFuncionais.selecionarOperador()
        self.resultado = DadosFuncionais.calcularResultado(self.num1, self.num2, self.operador_correto)

        cabecalho = tk.Frame(root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{partida_atual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(pontos)).grid(row=0, column=3, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", command=self.pararJogo)
        botao_parar.grid(row=0, column=4, padx=10)

        numeros_frame = tk.Frame(root)
        numeros_frame.pack(pady=40)
        tk.Label(numeros_frame, text=str(self.num1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text=str(self.num2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numeros_frame, text=str(self.resultado), font=("Arial", 32)).pack(side="left", padx=10)

        operacoes_frame = tk.Frame(root)
        operacoes_frame.pack(pady=30)

        operadores_mapeados = {"+": "+", "-": "-", "x": "*", "÷": "/"}

        for texto_botao, operador_real in operadores_mapeados.items():
            botao = tk.Button(
                operacoes_frame,
                text=texto_botao,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda op=operador_real: self.processarResposta(op)
            )
            botao.pack(side="left", padx=10)

        rodape = tk.Label(
            root,
            text="Desenvolvido por: \nJoão Silva e Maria Souza (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
    
    def processarResposta(self, resposta):
        if resposta == self.operador_correto:
            self.root.pontos += 199
        else:
            self.root.pontos += 0

        self.root.continua_jogo.set(True)
    
    def pararJogo(self):
        self.root.running = False
        self.root.continua_jogo.set(True)