from random import random

# Meminta input jumlah data
n = int(input("Masukkan nilai N: "))

i = 0
while i < n:
    a = random()  # menghasilkan angka acak 0.0 - 1.0
    if a < 0.5:
        print(f"data ke-{i+1} = {a}")
    i += 1

print("Selesai")