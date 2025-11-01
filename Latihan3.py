# Latihan 3: Simulasi Mesin ATM Sederhana

saldo = 1000000  # saldo awal Rp 1.000.000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        if jumlah > saldo:
            print("Saldo tidak cukup!")
        elif jumlah <= 0:
            print("Jumlah penarikan tidak valid!")
        else:
            saldo -= jumlah
            print("Penarikan berhasil!")
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
    
    if saldo == 0:
        print("Saldo Anda sudah habis. Terima kasih telah menggunakan ATM!")
        break