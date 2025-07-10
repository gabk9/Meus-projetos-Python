n1 = float(input("Me diga um número: "))
n2 = float(input("Me diga outro número: "))

media = (n1 + n2) / 2
div = n1 / n2
rest = n1 % n2
soma = n1 + n2
multi = n1 * n2
sub = n1 - n2

print(f"\nA media entre {n1: .2f} e {n2: .2f} é: {media: .2f}")
print(f"\nA divisão entre {n1: .2f} e {n2: .2f} é: {div: .2f}")
print(f"\nO resto da divisão entre {n1: .2f} e {n2: .2f} é: {rest: .2f}")
print(f"\nA soma entre {n1: .2f} e {n2: .2f} é: {soma: .2f}")
print(f"\nA multiplicação entre {n1: .2f} e {n2: .2f} é: {multi: .2f}")
print(f"\nA subtração entre {n1: .2f} e {n2: .2f} é: {sub: .2f}")

soma += n1
print(f"\nO valor da soma de ({n1: .2f} + {n2: .2f}) + {n1: .2f} é: {soma: .2f}")
sub -= n1
print(f"O valor da subtração de ({n1: .2f} - {n2: .2f}) - {n1: .2f} é: {sub: .2f}")