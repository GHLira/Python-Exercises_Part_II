#Obtenha os valores de a, b e c na equação quadrática 
# ax2 + bx + c. Calcule e apresente as raízes reais da 
# equação, usando a fórmula de Bhaskara. Considere apenas 
# os casos em que as raízes podem ser reais.

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta >= 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    
    if delta > 0:
        print(f"As raízes reais são distintas: x1 = {raiz1} e x2 = {raiz2}")
    else:
        print(f"A equação tem uma raiz real igual: x1 = x2 = {raiz1}")
else:
    print("A equação não possui raízes reais.")
