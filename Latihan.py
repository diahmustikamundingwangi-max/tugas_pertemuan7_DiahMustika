def menu():
    print("\n--- Menu Pilihan ---")
    print("1. Barisan Fibonacci")
    print("2. Perkalian M x N")
    print("0. Keluar")
    
while True:
    menu()
    pilihan = input("Pilih Menu: ")
    
    if pilihan == '1':
        print("Menjalankan program Fibonacci...")
        
    elif pilihan == '2':
        m = int(input("Masukkan M: "))
        n = int(input("Masukkan N: "))
        print(f"Hasil {m} x {n} adalah {m * n}")
    elif pilihan == '0':
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid!")