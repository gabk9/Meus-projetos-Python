def func(list):
    list = sorted(list)
    return list[-2]

def main():
    myList = []

    while 1:
        qty = int(input("Type-in the quantity of numbers in the list: "))

        if qty < 2:
            print("Please, only use numbers greater than 1")
            continue
        else: break

    for i in range(qty):
        num = int(input(f"Type-in the number n{i + 1}: "))
        myList.append(num)

    secNumber = func(myList)

    print("\nThe second biggest number in the list is: ", secNumber)

if __name__ == "__main__":
    main()