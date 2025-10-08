import random, os, msvcrt

def Cls():
    os.system('cls')

def Pause():
    print("\nPress any key to continue...\n")
    msvcrt.getch()

def main():
    secretNum = random.randint(1, 100)
    tries = 0 #the max will be 5
    tittle = "Guessing game"

    while 1:
        print(f"{tittle:=^25}")
        num = int(input("Type-in your guess: "))

        if tries >= 10:
            print("You don't have any tries left, Game Over!!")
            Pause()
            Cls()
            break

        if num < secretNum:
            print("The number you just typed is smaller than the secret one!")
            tries += 1
            Pause()
            Cls()
        elif num > secretNum:
            print("The number you just typed is greater than the secret one!")
            tries += 1
            Pause()
            Cls()
        else:
            print("You got it!! the numbers are the same!!")
            Pause()
            Cls()




if __name__ == "__main__":
    main()