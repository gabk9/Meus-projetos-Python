def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Me diga um número: "))
y = int(input("Me diga outro número: "))

maxDiv = mdc(x, y)

print(f"O maximo divisor comum entre {x} e {y} é: {maxDiv}") 