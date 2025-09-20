import os, json, time, platform, getpass, pyfiglet
from colorama import init, Fore, Back, Style
from dataclasses import dataclass

init(autoreset=True)


@dataclass
class Client:
    id: int
    name: str
    cpf: int
    telNumber: str

@dataclass
class Vehicle:
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

def vRegist(*files: str) -> None:
    cls()
    vehicles: list = []

    '''
        files[0] = Vehicles.json
    '''

    try:
        with open(files[0], "r", encoding="utf-8") as f:
            data: str = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data: list = []

    last_id: int = data[-1]["id"] + 1 if data else 1

    while True:
        print(f'{"Registrando":=^21}')
        try: 
            qtd: int = int(input("Quantos veículos deseja adicionar? "))
        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue
        
        for i in range(qtd):
            try:
                print(f"\n[{i + 1}]")
                vName: str = input("   Digite o nome do carro: ")
                vDate: int = int(input("   Digite o ano do carro (YYYY): "))
                vPrice: float = float(input("   Digite o preço do carro em R$: "))

                v = Vehicle(id=last_id, name=vName, date=str(vDate), price=vPrice)
                vehicles.append(v)

                data.append(v.__dict__)  
                last_id += 1

            except ValueError:
                print("Valor inválido!!")
                pause()
                cls()
        
        with open(files[0], "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("\nVeículo(s) salvo(s) com sucesso!!")
        pause()
        cls()
        break

def vCheck(*files: str) -> None:
    cls()

    '''
        files[0] = Vehicles.json
    '''

        
    while True:
        print(f'{"Consultar veículos":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)
        
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break
        

        for v in data:
            print(f"\nId: {v["id"]} | Modelo: {v["name"]}\n")

        try:
            op: int = int(input("Digite o Id do carro desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        vehicle: int = next((v for v in data if v["id"] == op), None)

        if vehicle:
            print(f"\n\nId: {vehicle['id']} | Modelo: {vehicle['name']}")
            print(f"Ano de lançamento: {vehicle['date']} | Preço: {vehicle['price']:.2f}R$\n")
            pause()
            cls()
            break
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue

def vUpdate(*files: str) -> None:
    cls()

    '''
        files[0] = Vehicles.json
    '''
        
    while True:
        print(f'{"Atualizar veículos":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)
        
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break


        for v in data:
            print(f"\nId: {v['id']} | Modelo: {v['name']}\n")

        try:
            op: int = int(input("Digite o Id do carro desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        vehicle: int = next((v for v in data if v['id'] == op), None)

        if vehicle:
            print(f"\n\nId: {vehicle['id']} | Modelo: {vehicle['name']}")
            print(f"Ano de lançamento: {vehicle['date']} | Preço: {vehicle['price']:.2f}R$\n")

            print("Deixe em branco para não alterar.\n")

            newName: str = input("Digite o novo modelo: ").strip()
            newDate: str = input("Digite o novo ano de lançamento: ").strip()
            newPrice: str = input("Digite o novo preço em R$: ").strip()
            

            if newName:
                vehicle['name'] = newName
            if newDate:
                try:
                    vehicle['date'] = int(newDate)
                except ValueError:
                    print("Ano inválido, ignorando alteração.")
            if newPrice:
                try:
                   vehicle['price'] = float(newPrice.replace(",", "."))
                except ValueError:
                    print("Preço inválido, ignorando alteração.")

            with open(files[0], "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            print("\nNovos Dados salvos com sucesso!!")
            pause()
            cls()
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue

def vFileRemove(*files: str) -> None:
    password: str = input("\nDigite a senha padrão: ")

    '''
        files[0] = Vehicles.json
        files[1] = DEFAULT_PASSWORD
    '''

    if password != files[1]:
        print("Senha inválida!!")
        pause()
        cls()
        return
    
    cls()
    while True:
        print(f'{"Removendo veículos":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break

        for v in data:
            print(f"\nId: {v["id"]} | Modelo: {v["name"]}\n")

        try:
            op: int = int(input("Digite o Id do carro desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        vehicle: int = next((v for v in data if v["id"] == op), None)
        
        if vehicle:
            print(f"\nId: {vehicle['id']} | Modelo: {vehicle['name']}")
            print(f"Ano: {vehicle['date']} | Preço: {vehicle['price']:.2f}R$")

            confirm = input("\nDeseja realmente remover este veículo? (s/n): ").lower()
            if confirm == "s":
                data.remove(vehicle)

                for i, v in enumerate(data, start=1):
                    v['id'] = i

                with open(files[0], "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                print("\nVeículo removido com sucesso!!")
                pause()
                cls()
                return
            else:
                print("\nRemoção cancelada!!")
                pause()
                cls()
                continue
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue


def vehiclesMenu(*data: str) -> None:
    cls()

    '''
        data[0] = Vehicles.json
        data[1] = Purchases.json # TODO: add Purchases.json sync
        data[2] = DEFAULT_PASSWORD
    '''

    if not hasattr(vehiclesMenu, "typeSpeed"):
        vehiclesMenu.typeSpeed = 7

    while True:
        print(f'{"Seção Veículos":=^24}')
        type("[1] Registrar veículos\n[2] Consultar veículos\n[3] Atualizar veículos\n", vehiclesMenu.typeSpeed)
        type("[4] Deletar veículos\n[5] Deletar todos os veículos\n[0] Voltar para o menu principal\n", vehiclesMenu.typeSpeed)
        vehiclesMenu.typeSpeed = 0

        try:
            op: int = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                vRegist(data[0])
            case 2:
                vCheck(data[0])
            case 3:
                vUpdate(data[0], data[1])
            case 4:
                vFileRemove(data[0], data[2])
            case 5:
                password: str = input("\nMe diga a senha padrão: ")
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

def cRegist(*files: str) -> None:
    cls()
    clients: list = []

    '''
        files[0] = Clients.json
    '''

    try:
        with open(files[0], "r", encoding="utf-8") as f:
            data: str = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data: list = []

    last_id: int = data[-1]["id"] + 1 if data else 1

    while True:
        print(f'{"Registrando":=^21}')
        try: 
            qtd: int = int(input("Quantos clientes deseja adicionar? "))
        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue
        
        for i in range(qtd):
            print(f"\n[{i + 1}]")
            vName: str = input("   Digite o nome do cliente: ")
            vCpf: str = input("   Digite o cpf do cliente: ")
            vTelNum: str = input("   Digite o número de telefone do cliente ((AA) NNNNN-NNNN): ")

            c = Client(id=last_id, name=vName, cpf=vCpf, telNumber=vTelNum)
            clients.append(c)

            data.append(c.__dict__)  
            last_id += 1

        
        with open(files[0], "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("\nCliente(s) salvo(s) com sucesso!!")
        pause()
        cls()
        break

def cCheck(*files: str) -> None:
    cls()

    '''
        files[0] = Clients.json
    '''

        
    while True:
        print(f'{"Consultar clientes":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)
        
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break
        

        for c in data:
            print(f"\nId: {c["id"]} | Nome: {c["name"]}\n")

        try:
            op: int = int(input("Digite o Id do cliente desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        client: int = next((c for c in data if c["id"] == op), None)

        if client:
            print(f"\n\nId: {client['id']} | Nome: {client['name']}")
            print(f"Cpf: {client['cpf']} | Número de telefone: {client['telNumber']}\n")
            pause()
            cls()
            break
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue

def cUpdate(*files: str) -> None:
    cls()

    '''
        files[0] = Clients.json
    '''
        
    while True:
        print(f'{"Atualizar clientes":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)
        
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break


        for v in data:
            print(f"\nId: {v['id']} | Nome: {v['name']}\n")

        try:
            op: int = int(input("Digite o Id do cliente desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        client: int = next((c for c in data if c['id'] == op), None)

        if client:
            print(f"\n\nId: {client['id']} | Nome: {client['name']}")
            print(f"Cpf: {client['cpf']} | Número de telefone: {client['telNumber']}\n")

            print("Deixe em branco para não alterar.\n")

            newName: str = input("Digite o novo modelo: ").strip()
            newCpf: str = input("Digite o novo cpf: ").strip()
            newTelNumber: str = input("Digite o novo número de telefone ((AA) NNNNN-NNNN): ").strip()
            

            if newName:
                client['name'] = newName
            if newCpf:
                client['cpf'] = newCpf
            if newTelNumber:
                client['telNumber'] = newTelNumber
            with open(files[0], "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            print("\nNovos Dados salvos com sucesso!!")
            pause()
            cls()
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue

def cFileRemove(*files: str) -> None:
    password: str = input("\nDigite a senha padrão: ")

    '''
        files[0] = Vehicles.json
        files[1] = DEFAULT_PASSWORD
    '''

    if password != files[1]:
        print("Senha inválida!!")
        pause()
        cls()
        return
    
    cls()
    while True:
        print(f'{"Removendo clientes":=^28}')
        try:
            with open(files[0], "r", encoding="utf-8") as f:
                data: str = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            print("\nArquivo não encontrado!!\n")
            pause()
            cls()
            break

        for c in data:
            print(f"\nId: {c['id']} | Nome: {c['name']}\n")

        try:
            op: int = int(input("Digite o Id do carro desejado (0 para sair): "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        if op == 0:
            cls()
            break

        client: int = next((c for c in data if c['id'] == op), None)
        
        if client:
            print(f"\n\nId: {client['id']} | Nome: {client['name']}")
            print(f"Cpf: {client['cpf']} | Número de telefone: {client['telNumber']}\n")

            confirm = input("\nDeseja realmente remover este Cliente? (s/n): ").lower()
            if confirm == "s":
                data.remove(client)

                for i, c in enumerate(data, start=1):
                    c['id'] = i

                with open(files[0], "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                print("\nCliente removido com sucesso!!")
                pause()
                cls()
                return
            else:
                print("\nRemoção cancelada!!")
                pause()
                cls()
                continue
        else:
            print("Id não encontrado!!")
            pause()
            cls()
            continue


def clientsMenu(*data) -> None:
    cls()
    
    '''
        data[0] = Clients.json
        data[1] = Purchases.json # TODO: add Purchases.json sync
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
            op: int = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                cRegist(data[0])
            case 2:
                cCheck(data[0])
            case 3:
                cUpdate(data[0])
            case 4:
                cFileRemove(data[0], data[2])
            case 5:
                password: str = input("\nDigite a senha padrão: ")

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

def purchasesMenu(*data) -> None:
    cls()

    '''
        data[0] = Purchases.json
        data[1] = DEFAULT_PASSWORD
    '''

    if not hasattr(purchasesMenu, "typeSpeed"):
        purchasesMenu.typeSpeed = 8

    while True:
        print(f'{"Seção vendas":=^22}')
        type("[1] Listar vendas\n[2] Deletar vendas\n[3] Deletar todas as vendas\n", purchasesMenu.typeSpeed)
        type("[0] Voltar para o menu principal", purchasesMenu.typeSpeed)
        purchasesMenu.typeSpeed = 0

        try:
            op: int = int(input("\nEscolha uma opção: "))

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
                password: str = input("\nDigite a senha padrão: ")

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

def Sleep(ms: int) -> None:
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
            op: int = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nValor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                cls()
                strings: str = ("Feito por Gabriel Oliveira Miranda",
                                "Um estudante do primeiro ano",
                                "Esse código ainda está em beta!")
                
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
    
    '''
        data[0] = Clients.json
        data[1] = Vehicles.json
        data[2] = Purchases.json 
        data[3] = DEFAULT_PASSWORD
    '''

    password: str = input("\nMe diga a senha padrão: ")
    
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


def main() -> None:
    op: int = 0
    typeSpeed: int = 6

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

    ascii_art: str = pyfiglet.figlet_format("MEU CRUD")

    print(Fore.RED + Back.BLACK + ascii_art + Style.RESET_ALL)
    Vload(25, 50)
    cls()

    while True:
        print(f'{"Concessionaria":=^24}')
        type("[1] Seção de veículos\n[2] Seção de clientes\n[3] Seção de vendas\n", typeSpeed)
        type("[4] Créditos\n[5] Deletar todos os dados\n[0] Sair\n", typeSpeed)
        typeSpeed: int = 0

        try:
            op = int(input("Escolha uma opção: ")) 
            #! On Linux it just keeps going to "case _:" whenever i compile the code, i couldn't fix it

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
                credits()
            case 5:
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