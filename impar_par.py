#Obtenha um número inteiro, verifique se o número é par ou ímpar, 
#imprima uma mensagem indicando se é par ou ímpar.
n1 = int(input("Digite um número inteiro: "))

if n1 % 2 == 0:
    print(f"O número {n1} é par.")
else:
    print(f"O número {n1} é ímpar.")
