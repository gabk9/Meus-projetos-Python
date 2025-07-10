import math
import os

n1 = int(input("Me diga um número: "))
n2 = int(input("Me diga outro número: "))

print(f"\nA raiz quadrada de {n1: d} é: {math.sqrt(n1): .2f}")
print(f"A potênciação de {n1: d} elevado à {n2: d} é: {math.pow(n1, n2)}")

os.system("cls")
print(f"\n{os.listdir()}")