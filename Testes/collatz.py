def collatz(n: int) -> int:
    seq = [n]

    while n != 1 and n != 0:
        
        if n % 2 == 0:
            n //= 2

        else:
            n = n * 3 + 1
        seq.append(n)

    return seq
    
def main():
    num: int = 1
    while True:
        num = int(input("Me diga um número (0 para sair): "))

        if num == 0:
            break

        lista = collatz(num)

        print(f"Sequência Collatz do número {num}: {lista}")
        break

if __name__ == "__main__":
    main()