# Latihan 2: Menghitung total laba selama 8 bulan

modal = 100000000  # modal awal 100 juta
laba = 0           # variabel total laba

for bulan in range(1, 9):  # perulangan dari bulan ke-1 sampai ke-8
    if bulan == 1 or bulan == 2:
        persen = 0
    elif bulan == 3 or bulan == 4:
        persen = 1
    elif bulan == 5 or bulan == 6 or bulan == 7:
        persen = 5
    elif bulan == 8:
        persen = 3
    
    # hitung laba bulan ini
    laba_bulan_ini = modal * persen / 100
    laba += laba_bulan_ini
    
    print(f"Laba bulan ke-{bulan} sebesar: {laba_bulan_ini}")

# total laba setelah 8 bulan
print(f"\nTotal laba adalah: {laba}")