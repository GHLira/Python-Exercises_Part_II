#Obtenha três valores positivos, representando os lados de um 
# triângulo, verifique se os valores formam um triângulo. Se formarem, determine 
# se é escaleno, isósceles ou equilátero. Calcule e imprima a área do triângulo usando a 
# fórmula de Heron. Caso não formem um triângulo, exiba uma mensagem informando isso.

import math

def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def calcular_area_heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Digite o valor do lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if verificar_triangulo(a, b, c):
    tipo = classificar_triangulo(a, b, c)
    area = calcular_area_heron(a, b, c)
    print(f"O triângulo é {tipo}.")
    print(f"A área do triângulo é: {area:.2f}")
else:
    print("Os valores não formam um triângulo.")
