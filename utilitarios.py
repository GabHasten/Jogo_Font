import tkinter as tk

def resetaTela(root):
    for widget in root.winfo_children():
        widget.destroy()

def rodape(value):
    rodape = tk.Label(value,text="Desenvolvido por\nGabriel Hatenreiter,Isabelle Dias e Vitoria Santos")
    rodape.pack(side="bottom",pady=10)
        
 
 #dentro da função da tela de instruções "limpamos" o que estava na tela para
 #mostrar os elementos da tela da instrução "nome_da_funcao_destroy(self.root)"