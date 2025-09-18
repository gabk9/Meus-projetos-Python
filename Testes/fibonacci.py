def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fib(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def main():
    num = int(input("Me diga um número: "))

    print(f"Sequência de fibonacci até o {num}° número: ", fib(num))
if __name__ == "__main__":
    main()