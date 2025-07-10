import getpass

validN = [1, 2, 3, 4, 5]
r = int(input("Me diga um número: "))

if r in validN:
    print("Número válido")
else:
    print("Número inválido")

n = float(getpass.getpass("\nMe diga sua nota: ")) # o número fica oculto ao digitar

if n >= 7.0:
    print("Aprovado!!")
elif n < 7.0 and n > 4.0:
    print("Tem direito a recuperação!")
else: 
    print("Reprovado!!")

