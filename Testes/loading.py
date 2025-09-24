from time import sleep

def loading(ms: int, lc: int) -> None:
    ASCII = ["\r\\", "\r|", "\r/", "\r-"]
    for _ in range(lc):
        for char in ASCII:
            print(char, end="", flush=True)
            sleep(ms / 1000)

def main() -> None:

    loading(75, 50)

if __name__ == "__main__":
    main()