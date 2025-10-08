import math

def busca_binaria(lista: list, alvo: int) -> int:
    inicio: int = 0
    fim: int = len(lista) - 1
    comparacoes: int = 0

    print(f"\nBuscando {alvo} em {len(lista)} elementos:")
    
    while inicio <= fim:
        meio: int = (inicio + fim) // 2
        comparacoes += 1
        print(f"Passo {comparacoes}: inicio={inicio}, fim={fim}, meio={meio}, valor={lista[meio]}")

        if lista[meio] == alvo:
            print(f"\nAlvo {alvo} encontrado no índice {meio} em {comparacoes} comparações.")
            return meio
        elif lista[meio] < alvo:
            inicio: int = meio + 1
        else:
            fim: int = meio - 1 

    print(f"\nAlvo {alvo} não encontrado após {comparacoes} comparações.")
    return -1

def main():
    n: int = int(input("Digite o tamanho da lista: "))
    lista: list = list(range(1, n+1))
    alvo: int = int(input("Digite o valor a buscar: "))

    log_valor: float = math.log2(n)
    passos_max: int = math.ceil(log_valor)
    print(f"\nlog2({n}) = {log_valor:.4f}")
    print(f"Passos máximos teóricos (ceil): {passos_max}")

    busca_binaria(lista, alvo)

if __name__ == "__main__":
    main()
