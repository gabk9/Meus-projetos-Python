import random, time, os, msvcrt, winsound

def cls():
    os.system("cls")

def Sleep(ms):
    time.sleep(ms / 1000)

def pause():
    print("Pressione qualquer tecla para continuar...")
    msvcrt.getch()

def type(texto, ms):
    for i in range(len(texto)):
        print(texto[i], end="", flush=True)
        Sleep(ms)

def chamar(listaP, listaN, senhasChamadas):
    cls()

    proxSenha = None
    if listaP:
        proxSenha = min(listaP)
        listaP.remove(proxSenha)
        senhasChamadas.append(f"P{proxSenha}")
    elif listaN:
        proxSenha = min(listaN)
        listaN.remove(proxSenha)
        senhasChamadas.append(f"N{proxSenha}")

    if proxSenha is not None:
        winsound.Beep(1000, 300)

        print("=" * 30)
        print("   >>> SENHA CHAMADA <<<")
        prefixo = "P" if senhasChamadas[-1].startswith("P") else "N"
        print(f"\n       {prefixo}{proxSenha}\n")
        print("=" * 30)
    else:
        print("Nenhuma senha na fila!")

    pause()

def PegarSenha(listaP, listaN, senhasUsadas):
    cls() 
    typeSpeed = 7

    while True:
        print("=== Pegar senha ===")
        type("[1] Normal\n[2] Prioritário\n[0] Voltar\n", typeSpeed)
        sp = input("Escolha uma opção: ").strip()
        typeSpeed = 0

        match sp:
            case "1":
                senha = gerarSenha(senhasUsadas)
                senhasUsadas.append(senha)
                listaN.append(senha)
                print(f"Sua senha é: N{senha}")
                pause()
                break

            case "2":
                senha = gerarSenha(senhasUsadas)
                senhasUsadas.append(senha)
                listaP.append(senha)
                print(f"Sua senha é: P{senha}")
                pause()
                break

            case "0":
                break

            case _:
                print("Opção inválida!!")
                pause()
                cls()

def gerarSenha(listaSenha):
    while True:
        senha = random.randint(1, 100)
        if senha not in listaSenha:
            return senha

def verFila(listaP, listaN):
    cls()
    print("=== Fila Atual ===")
    fila = sorted([f"P{n}" for n in listaP]) + sorted([f"N{n}" for n in listaN])
    if fila:
        for senha in fila:
            print(senha)
    else:
        print("Fila vazia!")
    pause()

def verFilaCompleta(listaP, listaN, senhasChamadas):
    cls()
    print("=== Fila Completa ===")
    print("Já chamadas:", " ".join(senhasChamadas) if senhasChamadas else "Nenhuma")
    print("Prioritárias pendentes:", " ".join(f"P{n}" for n in sorted(listaP)) if listaP else "Nenhuma")
    print("Normais pendentes:     ", " ".join(f"N{n}" for n in sorted(listaN)) if listaN else "Nenhuma")
    pause()

def main():
    typeSpeed = 15
    titulo = "Chamada de senhas"
    senhasUsadas = []
    senhasChamadas = []
    listaP = []
    listaN = []

    while True:
        cls()
        print(f"{titulo:=^29}")
        type("[1] Chamar próxima senha\n[2] Pegar senha\n[3] Ver fila\n[4] Ver fila completa\n[0] Sair\n", typeSpeed)
        op = input("Escolha uma opção: ").strip()
        typeSpeed = 0

        match op:
            case "1":
                chamar(listaP, listaN, senhasChamadas)

            case "2":
                PegarSenha(listaP, listaN, senhasUsadas)

            case "3":
                verFila(listaP, listaN)

            case "4":
                verFilaCompleta(listaP, listaN, senhasChamadas)

            case "0":
                print("Saindo do programa, tenha um bom dia...")
                pause()
                break

            case _:
                print("Opção inválida!!")
                pause()
                cls()

if __name__ == "__main__":
    main()
