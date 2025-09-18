while True:
    h = int(input("\n\nMe diga a altura: "))
    l = int(input("Me diga a largura: "))

    if l < 2 or h < 2:
        print("Diga valores maiores que 2!!")
        continue

    for alt in range(h):
        for wid in range(l):
            if alt == 0 or alt == h - 1 or wid == 0 or wid == l - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print()
    print() 

    for i in range(h):
        print("*" * l)