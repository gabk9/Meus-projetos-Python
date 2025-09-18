def primo(n) :
    if n < 2: return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    lista = [1, 2, 4, 5, 6, 7, 8, 9]
    primos = [x for x in lista if primo(x)]

    print("Primos: ", primos)
if __name__ == "__main__":
    main()