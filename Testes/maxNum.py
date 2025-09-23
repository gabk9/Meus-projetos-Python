from random import randint

FILE: str = "maxNum.txt"

while True:
    try:
        with open(FILE, "r") as f:
            content: str = f.read()
            nums = [int(value) for value in content.split()]
            print("O maior número desse .txt é: ", max(nums))
            break
            
    except FileNotFoundError:
        with open(FILE, "w") as f:
            for _ in range(10 ** 5):
                f.write(f"{randint(1, 10 ** 6)} ")