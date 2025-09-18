import os, json, time, platform, getpass, pyfiglet, sys
from colorama import init, Fore, Back, Style
from dataclasses import dataclass
from datetime import datetime

init(autoreset=True)


@dataclass
class client:
    id: int
    name: str
    cpf: int
    telephoneNumber: str

@dataclass
class vehicle:
    id: int
    name: str
    date: str
    price: float

@dataclass
class purchases:
    purchaseId: int
    clientId: int
    clientName: str
    vehicleId: int
    vehicleName: str
    date: str
    price: float

def vehiclesMenu(*data):
    cls()

    '''
        data[0] = Vehicles.json
        data[1] = Purchases.json
        data[2] = DEFAULT_PASSWORD
    '''

    if not hasattr(vehiclesMenu, "typeSpeed"):
        vehiclesMenu.typeSpeed = 7

    while True:
        print(f'{"Seção Veículos":=^24}')
        type("[1] Registrar Veículos\n[2] Consultar veículos\n[3] Atualizar veículos\n", vehiclesMenu.typeSpeed)
        type("[4] Deletar veículos\n[5] Deletar todos os veículos\n[0] Voltar para o menu principal\n", vehiclesMenu.typeSpeed)
        vehiclesMenu.typeSpeed = 0

        try:
            op = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                raise NotImplementedError("Implementar Registrar veículos")
            case 2:
                raise NotImplementedError("Implementar Consultar veículos")
            case 3:
                raise NotImplementedError("Implementar Atualizar veículos")
            case 4:
                raise NotImplementedError("Implementar Deletar veículos")
            case 5:
                password = input("\nMe diga a senha padrão: ")

                if password == data[2]:
                    try:
                        os.remove(data[0])
                        print("Todos os veículos foram apagados com sucesso!!")
                        pause()
                        cls()

                    except FileNotFoundError:
                        print("O arquivo não existe!!")
                        pause()
                        cls()
                else:
                    print("senha inválida!!")
                    pause()
                    cls()
            case 0:
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

def clientsMenu(*data):
    cls()

    '''
        data[0] = Clients.json
        data[1] = Purchases.json
        data[2] = DEFAULT_PASSWORD
    '''

    if not hasattr(clientsMenu, "typeSpeed"):
        clientsMenu.typeSpeed = 7

    while True:
        print(f'{"Seção clientes":=^24}')
        type("[1] Cadastrar clientes\n[2] Consultar clientes\n[3] Atualizar clientes\n", clientsMenu.typeSpeed)
        type("[4] Deletar clientes\n[5] Deletar todos os clientes\n[0] Voltar para o menu principal\n", clientsMenu.typeSpeed)
        clientsMenu.typeSpeed = 0

        try:
            op = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                raise NotImplementedError("Implementar cadastrar clientes")
            case 2:
                raise NotImplementedError("Implementar Consultar clientes")
            case 3:
                raise NotImplementedError("Implementar Atualizar clientes")
            case 4:
                raise NotImplementedError("Implementar deletar clientes")
            case 5:
                password = input("\nDigite a senha padrão: ")

                if password == data[2]:
                    try:
                        os.remove(data[0])
                        print("Clientes removidos com sucesso!!")
                        pause()
                        cls()

                    except FileNotFoundError:
                        print("O arquivo não existe!!")
                        pause()
                        cls()
            case 0:
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

def purchasesMenu(*data):
    cls()

    '''
        data[0] = Purchases.json
        data[1] = DEFAULT_PASSWORD
    '''

    if not hasattr(purchases, "typeSpeed"):
        purchasesMenu.typeSpeed = 8

    while True:
        print(f'{"Seção vendas":=^22}')
        type("[1] Listar vendas\n[2] Deletar vendas\n[3] Deletar todas as vendas\n", purchasesMenu.typeSpeed)
        type("[0] Voltar para o menu principal", purchasesMenu.typeSpeed)
        purchasesMenu.typeSpeed = 0

        try:
            op = int(input("\nEscolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue
        
        match op:
            case 1:
                raise NotImplementedError("Implementar listar vendas")
            case 2:
                raise NotImplementedError("Implementar deletar vendas")
            case 3:
                password = input("\nDigite a senha padrão: ")

                if password == data[1]:
                    try:
                        os.remove(data[0])
                        print("Vendas removidas com sucesso!!")
                        pause()
                        cls()

                    except FileNotFoundError:
                        print("O arquivo não existe!!")
                        pause()
                        cls()
                else:
                    print("Senha inválida!!")
                    pause()
                    cls()
            case 0:
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

def pause() -> None:
    if platform.system() == "Windows":
        import msvcrt
        print("Pressione qualquer tecla para continuar...")
        msvcrt.getch()
    else:
        getpass.getpass("Pressione qualquer tecla para continuar...")

def Sleep(ms) -> None:
    time.sleep(ms / 1000)

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def type(text: str, ms: int) -> None:
    for i in text:
        print(i, end="", flush=True)
        Sleep(ms)

def delete(text: str, ms: int) -> None:
    for _ in range(len(text)):
        print("\b \b", end="", flush=True)
        Sleep(ms)

def Vload(ms: int, BarSize: int) -> None:
    for i in range(BarSize + 1):
        percent: float = (i * 100) / BarSize
        percent = (i * 100) / BarSize
        print("\r[", end="", flush=True)
        print("#"*i, end="", flush=True)
        print(" "*(BarSize-i), end="", flush=True)
        print(f"] {percent:3.0f}%", end="", flush=True)
        Sleep(ms)
    print()
    
def credits() -> None:
    cls()

    if not hasattr(credits, "typeSpeed"):
        credits.typeSpeed = 12
        
    while True:
        print(f'{"Tela de créditos":=^26}')
        type("[1] Ver créditos\n[0] Voltar para o Menu principal\n", credits.typeSpeed)
        credits.typeSpeed = 0
        try:
            op = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                cls()
                strings: str = ["Feito por Gabriel Oliveira Miranda",
                                "Um estudante do primeiro ano",
                                "Esse código ainda está em beta!"]
                
                loopCount: int = 0
                while loopCount < 3:
                    for i in range(len(strings)):
                        type(strings[i], 35)
                        Sleep(550)
                        delete(strings[i], 25)
                    loopCount += 1
                
                print("Chegou no final dos créditos, agora estamos voltando...")
                pause()
                cls()
                break
            case 0:
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

def deleteData(*data) -> None:
    cls()

    '''
        data[0] = Clients.json
        data[1] = Vehicles.json
        data[2] = Purchases.json 
        data[3] = DEFAULT_PASSWORD
    '''

    if not hasattr(deleteData, "typeSpeed"):
        deleteData.typeSpeed = 12

    cls()
    while True:
        print(f'{"Deletar Dados":=^23}')
        type("[1] Deletar tudo\n[0] Voltar para o menu principal\n", deleteData.typeSpeed)
        deleteData.typeSpeed = 0
        try:
            op = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                password = input("\nMe diga a senha padrão: ")
                
                if password == data[3]:
                    try:
                        os.remove(data[0])
                        os.remove(data[1])
                        os.remove(data[2])
                        print("Dados apagados com sucesso!!")
                        pause()
                        cls()

                    except FileNotFoundError:
                        print("Os arquivos não existem!!")
                        pause()
                        cls()
                else:
                    print("Senha inválida!!")
                    pause()
                    cls()
            case 0:
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

def main() -> None:
    typeSpeed: int = 6
    op: int = 0

    CLIENTS_FILE: str = "Clients.json"
    VEHICLES_FILE: str = "Vehicles.json"
    PURCHASE_RECORD: str = "Purchases.json"
    DEFAULT_PASSWORD: str = "0000"

    system: str = platform.system()

    match system:
        case "Windows":
            print("\nRodando no windows!!")
        case "Linux":
            print("\nRodando no Linux!!")
        case "Darwin":
            print("\nRodando no Mac!!")
        case _:
            print("\nSistema desconhecido")    

    ascii_art = pyfiglet.figlet_format("MEU CRUD")

    print(Fore.RED + Back.BLACK + ascii_art + Style.RESET_ALL)
    Vload(25, 50)
    cls()

    while True:
        print(f'{"Concessionaria":=^24}')
        type("[1] Seção de veículos\n[2] Seção de clientes\n[3] Seção de vendas", typeSpeed)
        type("\n[4] Salvar dados\n[5] Créditos\n[6] Deletar dados\n", typeSpeed)
        type("[0] Sair\n", typeSpeed)
        typeSpeed: int = 0

        try:
            op = int(input("Escolha uma opção: ")) 
            #! it just keeps going to "case _:" whenever i compile the code, i couldn't fix it

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                vehiclesMenu(VEHICLES_FILE, PURCHASE_RECORD, DEFAULT_PASSWORD)
            case 2:
                clientsMenu(CLIENTS_FILE, PURCHASE_RECORD, DEFAULT_PASSWORD)
            case 3:
                purchasesMenu(PURCHASE_RECORD, DEFAULT_PASSWORD)
            case 4:
                raise NotImplementedError("\nSalvar dados não implementado")
            case 5:
                credits()
            case 6:
                deleteData(CLIENTS_FILE, VEHICLES_FILE, PURCHASE_RECORD, DEFAULT_PASSWORD)
            case 0:
                print("\nSaindo, até depois!!")
                pause()
                cls()
                break
            case _:
                print("\nOpção inválida!!")
                pause()
                cls()

if __name__ == "__main__":
    main()