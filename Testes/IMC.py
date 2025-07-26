import msvcrt, os, time
from colorama import init, Fore, Style

init(autoreset = True)

def cls():
    os.system('cls')

def pause(msg="Pressione qualquer tecla para continuar..."):
    print(msg)
    msvcrt.getch()

def Result(altura, peso):
    altura /= 100
    imc = peso / (altura ** 2)

    print()
    if imc < 18.5:
        print(f"{Fore.LIGHTGREEN_EX}{imc} \nMagreza")
    elif imc >= 18.5 and imc < 25:
        print(f"{Fore.GREEN}{imc} \nNormal")
    elif imc >= 25 and imc < 30:
        print(f"{Fore.LIGHTRED_EX}{imc} \nSobrepeso")
    elif imc >= 30 and imc < 40:
        print(f"{Fore.RED}{imc} \nObesidade")
    else:
        print(f"{Fore.MAGENTA}{imc} \nObesidade Grave")
    pause()
    cls()

def Load(ms):
    for i in range(0, 101):
        print(f"{Fore.CYAN}\r[{i:3d}%]", end="", flush= True)
        time.sleep(ms / 1000)

def main():
    PESO = 0.0
    ALTURA = 0.0
    while(1):
        print(Fore.BLUE + "======Calculadora de IMC======")

        PESO = float(input(f"Me diga em KG, o seu{Fore.RED} peso: "))
        ALTURA = float(input(f"{Fore.WHITE}Agora me diga em centímetros, sua{Fore.GREEN} altura: "))

        print(f"O seu IMC é: ")

        Load(25)    

        print()
        Result(ALTURA, PESO)

if __name__ == "__main__":
    main()