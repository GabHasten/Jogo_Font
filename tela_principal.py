import tkinter as tk
from tkinter import messagebox

def janela_principal():

    root=tk.Tk()
    root.title("The Math Game ")
    root.geometry("800x600")
    root.resizable(False,False)
    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True

    def fechar_janela():

        if messagebox.askyesno("Confirmação","Você quer sair ?"):
            root.runnig = False
            root.continua_jogo.set(True) 
            root.destroy()

    root.protoc   ol("WM_DELETE_WINDOW", fechar_janela)
    return root

root = janela_principal()


root.mainloop()

try:
    root.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")

