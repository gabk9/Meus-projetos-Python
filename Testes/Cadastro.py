import json, os, msvcrt

ARQUIVO = "clientes.json"

def cls():
    os.system('cls')

def pause():
    print("Pressione qualquer tecla para continuar...")
    msvcrt.getch()

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salvar dados no arquivo
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def adicionar_cliente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")

    clientes = carregar_dados()
    for c in clientes:
        if c["cpf"] == cpf:
            print("CPF já cadastrado!")
            pause()
            return

    cliente = {"nome": nome, "idade": idade, "cpf": cpf}
    clientes.append(cliente)
    salvar_dados(clientes)
    print("Cliente adicionado com sucesso.")
    pause()
    cls()

def listar_clientes():
    clientes = carregar_dados()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for i, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {i}")
        print(f"Nome : {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"CPF  : {cliente['cpf']}")
        
    pause()
    cls()

def buscar_cliente():
    termo = input("Digite o nome ou CPF para buscar: ").lower()
    clientes = carregar_dados()
    encontrados = [c for c in clientes if termo in c["nome"].lower() or termo in c["cpf"]]
    if not encontrados:
        print("Cliente não encontrado.")
    else:
        for cliente in encontrados:
            print(f"\nNome : {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CPF  : {cliente['cpf']}")
    pause()
    cls()

def editar_cliente():
    cpf_alvo = input("Digite o CPF do cliente que deseja editar: ")
    clientes = carregar_dados()

    for cliente in clientes:
        if cliente["cpf"] == cpf_alvo:
            print("Cliente encontrado. Deixe em branco para manter o valor atual.")
            novo_nome = input(f"Novo nome ({cliente['nome']}): ") or cliente["nome"]
            nova_idade = input(f"Nova idade ({cliente['idade']}): ") or cliente["idade"]
            cliente["nome"] = novo_nome
            cliente["idade"] = nova_idade
            salvar_dados(clientes)
            print("Cliente atualizado com sucesso.")
            pause()
            cls()
            return

    print("Cliente com esse CPF não foi encontrado.")
    pause(cls)

def menu():
    while True:
        print("\n====MENU CLIENTES====")
        print("[1] Adicionar cliente")
        print("[2] Listar todos os clientes")
        print("[3] Editar cliente (por CPF)")
        print("[4] Buscar cliente")
        print("[5] Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            adicionar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            editar_cliente()
        elif op == "4":
            buscar_cliente()
        elif op == "5":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")
            pause()
            cls()

# Executar
menu()
