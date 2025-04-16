import tkinter as tk
import time
from tkinter import messagebox
from utilitarios import resetaTela, rodape
from logica_jogo import DadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.operador_correto = None
        self.num1 = None
        self.num2 = None
        self.resultado = None

        self.root.running = True
        self.root.pontos = 0
        self.root.acertos = 0
        self.root.continua_jogo = tk.BooleanVar(value=False)

        self.tempo_label = None
        self.time_id = None
        self.paused = False

        self.iniciaTempo = 0

        #controle de tempo
        self.tempo_pausado = 0 
        self.root.start_time = time.time()

    def frameTelaJogo(self, root, partida_atual, pontos):
        resetaTela(root)
        self.root.title("The Math Game")
        self.iniciaTempo = time.time()


        self.num1, self.num2 = DadosFuncionais.gerarNumeros()
        self.operador_correto = DadosFuncionais.selecionarOperador()
        self.resultado = DadosFuncionais.calcularResultado(self.num1, self.num2, self.operador_correto)

        cabecalho = tk.Frame(root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{partida_atual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(pontos)).grid(row=0, column=3, padx=10)

        tk.Label(cabecalho, text="Tempo:").grid(row=0, column=4, padx=10)
        self.tempo_label = tk.Label(cabecalho, text="00:00")
        self.tempo_label.grid(row=0, column=5, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", command=self.pararJogo)
        botao_parar.grid(row=0, column=6, padx=10)

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

        rodape(self.root)

        self.paused = False
        self.atualizarTempo()

    def atualizarTempo(self):
        if not self.root.running or self.paused:
            return

        #Calcula tempo total jogado até agora (considerando pausas)
        self.tempo_pausado = int(time.time() - self.root.start_time)
        minutos = self.tempo_pausado // 60
        segundos = self.tempo_pausado % 60
        self.tempo_label.config(text=f"{minutos:02d}:{segundos:02d}")

        self.time_id = self.root.after(1000, self.atualizarTempo)

    def processarResposta(self, resposta):
        if resposta == self.operador_correto:
            tempo_decorrido_questao = time.time() - self.iniciaTempo
            if tempo_decorrido_questao < 20:
                self.root.pontos += 199 * 10
            else:
                self.root.pontos += 199
            self.root.acertos += 1
        else:
            self.root.pontos += 0

        self.root.continua_jogo.set(True)

    def pararJogo(self):
        self.paused = True
        if self.time_id:
            self.root.after_cancel(self.time_id)
            self.time_id = None

        if messagebox.askyesno("Confirmação", "Você quer sair ?"):
            from tela_abertura import TelaInicial
            TelaInicial(self.root).constroiLayout()
        else:
            # ⏱️ Recalcula start_time ao voltar da pausa
            self.root.start_time = time.time() - self.tempo_pausado
            self.paused = False
            self.atualizarTempo()
