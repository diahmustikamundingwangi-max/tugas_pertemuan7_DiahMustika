def hitung_pangkat():
    print("\n--- Menu 1: Perpangkatan A^B ---")
    bilangan = int(input("masukkan suatu bilangan bulat : "))
    pangkat = int(input("masukkan pangkat yang diinginkan : "))
    
    hasil = 1
    for i in range(1, pangkat + 1):
        hasil = hasil * bilangan
        print(f"#hasil {bilangan} pangkat {i} adalah {hasil}")
        
def hitung_deret_pecahan():
    print("\n--- Menu 2: Hitung 1 - 2/3 + 5/8 - 13/21 + ... ---")
    n = int(input("Masukkan jumlah N : "))
    
    fib = [1, 1]
    for i in range(2, (2 * n) + 2):
        fib.append(fib[i-1] + fib[i-2])
        
    total = 0
    for i in range(n):
        pembilang = fib[i*2]
        penyebut = fib[i*2 + 1]
        suku = pembilang / penyebut
        
        if i % 2 == 0:
            total += suku
        else:
            total -= suku
            
    print(f"{total}")
    
while True:
    print("\n1. A pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
    print("0. keluar")
    
    pilihan = input("Masukkan : ")
    
    if pilihan == '1':
        hitung_pangkat()
    elif pilihan == '2':
        hitung_deret_pecahan()
    elif pilihan == '3':
        hitung_deret_pecahan()
    elif pilihan == '0':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak tersedia.")