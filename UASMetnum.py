def input_matriks(nama):
    baris = int(input(f"Masukkan jumlah baris Matriks {nama}: "))
    kolom = int(input(f"Masukkan jumlah kolom Matriks {nama}: "))
    matriks = []

    print(f"Masukkan elemen Matriks {nama}:")
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            val = int(input(f"{nama}[{i}][{j}]: "))
            baris_data.append(val)
        matriks.append(baris_data)

    return matriks, baris, kolom

def cetak_matriks(matriks):
    for baris in matriks:
        print("\t".join(str(x) for x in baris))

def jumlah_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def kali_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(A[0])):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil

def main():
    print("== PROGRAM OPERASI MATRIKS ==")
    print("1. Penjumlahan Matriks")
    print("2. Perkalian Matriks")
    pilihan = input("Pilih operasi (1/2): ").strip()

    print("\n== INPUT MATRIKS A ==")
    A, barisA, kolomA = input_matriks("A")

    print("\n== INPUT MATRIKS B ==")
    B, barisB, kolomB = input_matriks("B")

    if pilihan == "1":
        if barisA == barisB and kolomA == kolomB:
            print("\n== HASIL PENJUMLAHAN ==")
            hasil = jumlah_matriks(A, B)
            cetak_matriks(hasil)
        else:
            print("\n❌ Ukuran matriks tidak sama, tidak bisa dijumlahkan.")

    elif pilihan == "2":
        if kolomA == barisB:
            print("\n== HASIL PERKALIAN ==")
            hasil = kali_matriks(A, B)
            cetak_matriks(hasil)
        else:
            print("\n❌ Perkalian tidak bisa dilakukan karena kolom A ≠ baris B.")
    else:
        print("\n❌ Pilihan tidak valid.")

main()
