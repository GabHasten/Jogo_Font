import random as rd


num1 = rd.randint (0,9)
num2 = rd.randint (0,9)

operador = ["+","-","*","/"]
op_escolinhdo = rd.choice(operador)

if(op_escolinhdo == "+"):
    res = num1 + num2

elif(op_escolinhdo == "-"):
    res = num1 - num2

elif(op_escolinhdo == "*"):
    res = num1 * num2

else:
    res = num1 / num2

print(f"{num1} ? {num2} = {res}")

resU=input("Qual o operador desta questão ?: ")

if (resU != op_escolinhdo):
    print("Você errou !")
else:
    print("PARABÉNS !")