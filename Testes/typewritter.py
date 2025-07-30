import time

def type(texto, ms):
    for i in range(len(texto)):
        print(texto[i], end="", flush=True)
        time.sleep(ms / 1000)

def main():

    type("Olá mundo!!", 50)

if __name__ == "__main__":
    main() 