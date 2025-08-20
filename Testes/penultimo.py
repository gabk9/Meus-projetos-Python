def func(list):
    list = sorted(list)
    return list[-2]

def main():
    qty = int(input("Type-in the quantity of numbers in the list: "))
    myList = []

    for i in range(qty):
        num = int(input(f"Type-in the number n{i + 1}: "))
        myList.append(num)

    secNumber = func(myList)

    print("\nThe second biggest number in the list is: ", secNumber)

if __name__ == "__main__":
    main()