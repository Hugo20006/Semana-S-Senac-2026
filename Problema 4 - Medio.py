def adicao (a, b):
     return a+b 
def subtracao (a, b):
      
 multiplicacao (a, b)
      return a * b
def divisao (a, b):
      if b == 0:
          return "Erro: Divisão por zero não é permitida."
      return a / b
def potencia (a, ):
      return a ** b

numero1= float((" Digite o primeiro número: "))
= (input(" Digite o segundo número: ))

print("""
      Escolha a operação desejada:
       - adicao
      2 - Subtração
      3 - 
      4 - Divisao
      5 - Potência""")

operacão = (input("Digite o número da operacão desejada: ")

if operacão == "1":
   print("Resultado:", adicao(numero1, numero2))
elif operacão== "2":
   print("Resultado", subtracao(numero1,numero2))
elif operacão == "3":
   print("Resultado:", multiplicacao(numero1, numero2))
elif operacão == "4":
   print("Resultado:", divisao(numero1, numero2))
elif operacão == "5":
   print("Resultado:", (numero1, numero2))
else:
   ("Não achei a operacão desejada")

