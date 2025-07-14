import os
import msvcrt

def cls():
    os.system('cls')

def pause(msg="Pressione qualquer tecla para continuar..."):
    print(msg)
    msvcrt.getch()

dia = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]

def main():     
    n = 1
    while n != 0:
        cls()
        n = int(input("Me diga um número de 1 a 7, 0 para sair: "))

        if n < 0 or n > 7:
            print("Valor inválido!!")
            pause()
        elif n == 0:
            print("Saindo...")
            break
        else:
            print(f"Dia: {dia[n - 1]}")
            pause()
            
if __name__ == "__main__":
    main()
