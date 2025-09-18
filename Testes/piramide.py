import os

def Clear():
    os.system("cls")

def main():
    h = int(input(("Type-in the height: ")))
    b = (2 * h) - 1

    Clear()

    print("A pyramid with the height of: ", h)

    for x in range(h):
        Nhashes = (2 * x) + 1
        Nspaces = (b - Nhashes) // 2

        linha = " " * Nspaces + "#" * Nhashes
        print(linha)

if __name__ == "__main__":
    main()