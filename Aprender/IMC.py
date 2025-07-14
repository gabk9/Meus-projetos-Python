import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

class Dados:
    def __init__(self):
        self.peso = 0
        self.altura = 0
        self.idade = 0
        self.nome = ""
        self.IMC = 0.0

lista = Dados()

def typewriter(texto, delay_ms, cor=Fore.RESET):
    for c in texto:
        print(cor + c, end='', flush=True)
        time.sleep(delay_ms / 1000)
    print(Style.RESET_ALL, end='')  # Garante que reseta no final

def linha():
    print(Fore.LIGHTMAGENTA_EX + "\n------------------------------\n")

def comparacao_en():
    if lista.IMC < 18.5:
        print(Fore.RED + "\nUnderweight\n")
    elif lista.IMC < 25:
        print(Fore.YELLOW + "\nNormal weight\n")
    elif lista.IMC < 30:
        print(Fore.LIGHTRED_EX + "\nOverweight\n")
    else:
        print(Fore.RED + "\nObesity\n")

def comparacao_pt():
    if lista.IMC < 18.5:
        print(Fore.RED + "\nAbaixo do peso\n")
    elif lista.IMC < 25:
        print(Fore.YELLOW + "\nPeso normal\n")
    elif lista.IMC < 30:
        print(Fore.LIGHTRED_EX + "\nSobrepeso\n")
    else:
        print(Fore.RED + "\nObesidade\n")

def calcular_imc_en_im():
    lista.altura = float(input(f"Tell me your {Fore.GREEN}height{Style.RESET_ALL} in feet: "))
    lista.peso = float(input(f"Now tell me your {Fore.RED}weight{Style.RESET_ALL} in Lb's: "))
    altura_polegadas = lista.altura * 12
    lista.IMC = (lista.peso * 703) / (altura_polegadas ** 2)

def calcular_imc_en_m():
    lista.altura = float(input(f"Tell me your {Fore.GREEN}height{Style.RESET_ALL} in cm: "))
    lista.peso = float(input(f"Now tell me your {Fore.RED}weight{Style.RESET_ALL} in KG: "))
    altura_metros = lista.altura / 100
    lista.IMC = lista.peso / (altura_metros ** 2)

def calcular_imc_pt_im():
    lista.altura = float(input(f"Me diga sua {Fore.GREEN}altura{Style.RESET_ALL} em pés: "))
    lista.peso = float(input(f"Me diga seu {Fore.RED}peso{Style.RESET_ALL} em LB's: "))
    altura_polegadas = lista.altura * 12
    lista.IMC = (lista.peso * 703) / (altura_polegadas ** 2)

def calcular_imc_pt_m():
    lista.altura = float(input(f"Me diga sua {Fore.GREEN}altura{Style.RESET_ALL} em cm: "))
    lista.peso = float(input(f"Me diga seu {Fore.RED}peso{Style.RESET_ALL} em KG: "))
    altura_metros = lista.altura / 100
    lista.IMC = lista.peso / (altura_metros ** 2)

def mostrar_imc_en():
    os.system("cls" if os.name == "nt" else "clear")
    print("Your BMI is:", Fore.LIGHTCYAN_EX + f"{lista.IMC:.2f}" + Style.RESET_ALL)
    comparacao_en()
    input("Press ENTER to continue...")

def mostrar_imc_pt():
    os.system("cls" if os.name == "nt" else "clear")
    print("Seu IMC é:", Fore.LIGHTCYAN_EX + f"{lista.IMC:.2f}" + Style.RESET_ALL)
    comparacao_pt()
    input("Pressione ENTER para continuar...")

def en_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.LIGHTGREEN_EX + "\n===== BMI MENU =====\n" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] Show BMI" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] Recalculate" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] Return to previous menu" + Style.RESET_ALL)
        print(Fore.CYAN + "[4] Exit\n" + Style.RESET_ALL)
        linha()
        op = input("Choose an option: ")

        if op == '1':
            mostrar_imc_en()
        elif op == '2':
            calcular_imc_en_im()
        elif op == '3':
            break
        elif op == '4':
            print(Fore.LIGHTRED_EX + "\nLeaving... Cya!\n" + Style.RESET_ALL)
            exit(0)
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid option!\n" + Style.RESET_ALL)
            input("Press ENTER to continue...")

def pt_menu_im():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.LIGHTGREEN_EX + "\n===== MENU IMC =====\n" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] Mostrar IMC" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] Recalcular" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] Voltar" + Style.RESET_ALL)
        print(Fore.CYAN + "[4] Sair\n" + Style.RESET_ALL)
        linha()
        op = input("Escolha uma opção: ")

        if op == '1':
            mostrar_imc_pt()
        elif op == '2':
            calcular_imc_pt_im()
        elif op == '3':
            break
        elif op == '4':
            print(Fore.LIGHTRED_EX + "\nSaindo, até logo!\n" + Style.RESET_ALL)
            exit(0)
        else:
            print(Fore.LIGHTRED_EX + "\nOpção inválida!\n" + Style.RESET_ALL)
            input("Pressione ENTER para continuar...")

def sistema_menu_en():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.LIGHTGREEN_EX + "\n===== SYSTEM =====\n" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] Imperial" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] Metric" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] Return" + Style.RESET_ALL)
        print(Fore.CYAN + "[4] Exit\n" + Style.RESET_ALL)
        linha()
        op = input("Choose an option: ")

        if op == '1':
            calcular_imc_en_im()
            en_menu()
        elif op == '2':
            calcular_imc_en_m()
            en_menu()
        elif op == '3':
            break
        elif op == '4':
            print(Fore.LIGHTRED_EX + "\nLeaving... Cya!\n" + Style.RESET_ALL)
            exit(0)
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid option!\n" + Style.RESET_ALL)
            input("Press ENTER to continue...")

def sistema_menu_pt():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.LIGHTGREEN_EX + "\n===== SISTEMA =====\n" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] Imperial" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] Métrico" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] Voltar" + Style.RESET_ALL)
        print(Fore.CYAN + "[4] Sair\n" + Style.RESET_ALL)
        linha()
        op = input("Escolha uma opção: ")

        if op == '1':
            calcular_imc_pt_im()
            pt_menu_im()
        elif op == '2':
            calcular_imc_pt_m()
            pt_menu_im()
        elif op == '3':
            break
        elif op == '4':
            print(Fore.LIGHTRED_EX + "\nSaindo... Até logo!\n" + Style.RESET_ALL)
            exit(0)
        else:
            print(Fore.LIGHTRED_EX + "\nOpção inválida!\n" + Style.RESET_ALL)
            input("Pressione ENTER para continuar...")

def menu_principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.LIGHTGREEN_EX + "\n===== MENU =====\n" + Style.RESET_ALL)
        print(Fore.CYAN + "[1] English" + Style.RESET_ALL)
        print(Fore.CYAN + "[2] Português" + Style.RESET_ALL)
        print(Fore.CYAN + "[3] Exit\n" + Style.RESET_ALL)
        op = input("Answer/Resposta: ")

        if op == '1':
            os.system("cls" if os.name == "nt" else "clear")

            typewriter("Welcome to the BMI calculator!!\n", 40, Fore.LIGHTGREEN_EX)
            time.sleep(1)
            sistema_menu_en()
        elif op == '2':
            os.system("cls" if os.name == "nt" else "clear")
            typewriter("Seja bem vindo à calculadora de IMC!!\n", 40, Fore.LIGHTGREEN_EX)
            time.sleep(1)
            sistema_menu_pt()
        elif op == '3':
            print(Fore.LIGHTRED_EX + "\nLeaving/Saindo!\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.LIGHTRED_EX + "\nERROR/ERRO!!\n" + Style.RESET_ALL)
            input("Pressione ENTER para continuar...")

# Início
if __name__ == "__main__":
    menu_principal()