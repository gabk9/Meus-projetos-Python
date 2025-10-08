import os
import msvcrt
    
def cls():
    os.system('cls')

def pause(msg="Pressione qualquer tecla para continuar..."):
    print(msg)
    msvcrt.getch()

dia = ["\rSaindo...","Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]

def main():     
    n = 1
    while n != 0:
        n = int(input("Me diga um número de 1 a 7: "))
        print("Dia:", dia[n] if n >= 0 and n < len(dia) else "Opção inválida")
        pause()
        cls()
        
if __name__ == "__main__":
    main()
 