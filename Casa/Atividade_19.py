import random, time, msvcrt, os

def type(texto, ms):
    for i in range(len(texto)):
        print(texto[i], end="", flush=True)
        time.sleep(ms / 1000)

def pause():
    print("Pressione qualquer tecla para continuar...")
    msvcrt.getch()

def cls():
    os.system('cls')

def adivinhar(secreto):
    chutes = []
    escolha = 0
    tentativa = 1

    cls()
    while escolha != secreto:
        escolha = int(input("Me diga seu chute: "))

        if escolha in chutes:
            print("você já deu esse chute!!")
            pause()
            cls()

        else:
            chutes.append(escolha)

            if tentativa <= 10:

                if escolha <= 0:
                    print("Escolha um número maior que 0!!")
                    pause()
                    cls()
                    continue

                if escolha > secreto:
                    print("O número que você escolheu é maior que o secreto!")
                    tentativa += 1
                    pause()
                    cls()
                elif escolha < secreto:
                    print("O número que você escolheu é menor que o secreto!!")
                    tentativa += 1
                    pause()
                    cls()
                else:
                    print(f"Você acertou, o número secreto era {secreto}, e você acertou faltando {10 - tentativa} tentativas!!")
                    pause()
                    cls()
                    
            else:
                print("Game Over!!")
                pause()
                cls()


def main():
    typeSpeed = 7
    secreto  = random.randint(1, 100)
    op = None
    titulo = "JOGO DE ADIVINHAÇÃO"

    while op != 0:
        print(f"{titulo:=^25}")
        type("[1] Adivinha número\n[0] Encerrar programa", typeSpeed)
        typeSpeed = 0

        op = int(input("\nEscolha sua opção: "))

        match op:
            case 1:
                adivinhar(secreto)
            case 0:
                print("Encerrando o programa!!")
                pause()
                break
            case _:
                print("Insira um valor válido!!")
                pause()
                cls()

if __name__ == "__main__":
    main()