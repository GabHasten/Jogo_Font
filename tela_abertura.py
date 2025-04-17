import tkinter as tk
from tela_instrucoes import TelaInstrucoes
from utilitarios import resetaTela, rodape

class TelaInicial:
    def __init__(self,root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")


    def constroiLayout(self):
        tk.Label(self.root,text="The Math Game",bg="#262626",fg="#D99748",font=("Arial",30,"bold")).pack(pady=80,padx=0)
        
        button = tk.Button(self.root,text="Play",bg="#262626",fg="#D99748",command=self.abrirInstrucoes,font=("Arial",12))
        button.pack(padx=30,pady=10)

        rodape(self.root)
    

    def abrirInstrucoes(self):
        Tela_Instrucoes = TelaInstrucoes(self.root)
        Tela_Instrucoes.frameTelaInstrucoes()

