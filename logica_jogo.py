import random as rd
from tkinter import messagebox
from fim_jogo import FimJogo

class DadosOperacionais:
    @staticmethod
    def iniciaJogo(tela_jogo_instancia,root):
        contador = 1
        max_partidas = 20
        root.pontos = 0
        root.acertos = 0

        while contador <= max_partidas:
            tela_jogo_instancia.frameTelaJogo(root,contador,root.pontos)
            root.continua_jogo.set(False)
            root.wait_variable(root.continua_jogo)

            if not root.running:
                messagebox.showinfo("Jogo  encerrado","Você saiu do jogo")
                root.destroy()
                break
                

            contador +=1

        if contador > max_partidas:
            final = FimJogo(root, pontos=root.pontos, acertos=root.acertos, partidas=max_partidas)
            final.frameTelaFinal() 

    def abrirTelaFim(self):
        fim_jogo = FimJogo(self.root)
        fim_jogo.frameTelaFinal()


    @staticmethod
    def iniciaPartida(count,max):
        return count,max
    
    @staticmethod
    def iniciaPontos(score):
        return score


class DadosFuncionais:
    @staticmethod
    def gerarNumeros():
        num1 = rd.randint(0,9)
        num2 = rd.randint(0,9)
        return num1, num2

    @staticmethod
    def selecionarOperador():
        return rd.choice(["+","-","/","*"])

    @staticmethod
    def calcularResultado(a,b,op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return round(a/(b if b!=0 else 1),2)