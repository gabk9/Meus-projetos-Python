def maior(lista):
    return max(lista, key=len)

def main():
    palavras = []
    qtd = 5

    for i in range(qtd):
        string = input(f"Digite a palavra n{i + 1}: ")
        palavras.append(string)

    print("A maior palavra da lista é: ", maior(palavras))

if __name__ == "__main__":
    main()