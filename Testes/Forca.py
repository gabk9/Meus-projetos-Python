from random_word import RandomWords
import os, msvcrt

def cls():
    os.system('cls')

def pause(msg="Pressione qualquer tecla para continuar..."):
    print(msg)
    msvcrt.getch()

def main():
    letraEscolhida = []
    texto = "Jogo da forca"
    r = RandomWords()
    PalavraSecreta = r.get_random_word()

    if PalavraSecreta is None:
        print("Não foi possível gerar uma palavra.") 
        return

    PalavraSecreta = PalavraSecreta.lower()
    tentativas = len(PalavraSecreta) + 1

    while True:
        cls()
        print(f"{texto:-^36}")
        print(f"Essa palavra tem {len(PalavraSecreta)} letras\n")

        palavraMostrada = ""
        for l in PalavraSecreta:
            if l in letraEscolhida:
                palavraMostrada += l
            else:
                palavraMostrada += "_"
        print("Palavra: ", palavraMostrada)

        print(f"Letras já escolhidas: {', '.join(letraEscolhida)}")
        print("Tentativas: ", tentativas)

        if "_" not in palavraMostrada:
            print("Parabéns, você acertou a palavra!")
            break

        letra = input("\nDigite uma letra: ").lower()

        if letra not in PalavraSecreta and letra not in letraEscolhida:
            tentativas -= 1
            if tentativas == 0:
                print("\nGAME OVER!\n")
                break

        if letra in letraEscolhida:
            print("Você já disse essa letra.")
            pause()
            continue

        letraEscolhida.append(letra)

if __name__ == "__main__":
    main()
