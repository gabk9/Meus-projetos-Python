import time

def Load(ms):
    for i in range(101):
        print(f"\r[{i:3d}%]", end="", flush=True)
        time.sleep(ms / 1000)

def Vload(ms):
    total = 30 
    for i in range(total + 1):
        percent = (i * 100) / total
        print("\r[", end="", flush=True)
        
        for j in range(i):
            print("#", end="", flush=True)

        for k in range(total - i):
            print(" ", end="", flush=True)
            
        print(f"] {percent:3.0f}%", end="", flush=True)
        time.sleep(ms / 1000)

def main():
    Load(25)
    print()
    Vload(25)

if __name__ == "__main__":
    main()