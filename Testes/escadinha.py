import os

def cls():
    os.system('cls')

def main():
    alt = int(input("Me diga a altura: "))
    cls()

    for i in range(1, alt + 1):
        espacos = " " * (alt - i)
        degraus = "#" * i
        print(espacos + degraus + "  " + degraus)

main()