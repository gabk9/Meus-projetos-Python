import time

nums = int(input("Me diga quantos números deseja adicionar ao contador: "))
contador = 0

while True:
    while contador < nums:
        print(f"\rContador: {contador}%", end="", flush=True)
        time.sleep(25 / 1000)
        contador += 1

    entrada = input("\n\nDeseja adicionar mais? (0 para não adicionar) ")
    
    if entrada.strip() == "":
        break

    try:
        adicionar = int(entrada)
        if adicionar == 0:
            break
        else:
            nums += adicionar
    except ValueError:
        print("Entrada inválida. Digite um número.")
 