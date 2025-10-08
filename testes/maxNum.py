from random import randint
import os

FILE: str = "maxNum.txt"
MAXNUMS: int = 10**8
MAXGEN: int = 2**63
#! to generate 10⁸ 64bits numbers and find the max took 2mins and 13s, 1.85gb file, using hdd, i5-4690, 16gb of ram and using Linux
#! to generate 10⁸ 64bits numbers and find the max took 4mins and 36.3s, 1.94gb file, using ssd, i5-4690, 16gb of ram and using Windows

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        for _ in range(MAXNUMS):
            f.write(f"{randint(1, MAXGEN)}\n")

max: int = 0
with open(FILE, "r") as f:
    for line in f:
        n: int = int(line)
        if n > max:
            max: int = n

print("The biggest number of this .txt is:", max)
