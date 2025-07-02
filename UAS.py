def input_matriks(nama):
    baris = int(input(f"Masukkan jumlah baris Matriks {nama}: "))
    kolom = int(input(f"Masukkan jumlah kolom Matriks {nama}: "))
    matriks = []

    print(f"Masukkan elemen Matriks {nama}:")
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            val = float(input(f"{nama}[{i}][{j}]: "))
            baris_data.append(val)
        matriks.append(baris_data)

    return matriks, baris, kolom

def cetak_matriks(matriks):
    for baris in matriks:
        print("\t".join(str(round(x, 3)) for x in baris))

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

def input_augmented_matrix():
    n = int(input("Masukkan jumlah variabel (n): "))
    print(f"Masukkan koefisien dan hasil (augmented matrix {n} x {n+1}):")

    matrix = []
    for i in range(n):
        baris = []
        for j in range(n + 1):
            nilai = float(input(f"a[{i}][{j}]: "))
            baris.append(nilai)
        matrix.append(baris)
    return matrix, n

def cetak_augmented_matrix(matrix):
    for row in matrix:
        print(" | ".join(f"{x:7.3f}" for x in row[:-1]) + " || " + f"{row[-1]:7.3f}")
    print()

def gauss_jordan_elimination(matrix, n):
    print("\n== GAUSS-JORDAN ELIMINATION ==")
    solusi = [0] * n

    for i in range(n):
        # Pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Cek baris nol total
        if abs(matrix[i][i]) < 1e-9:
            all_zero = all(abs(matrix[i][j]) < 1e-9 for j in range(n))
            if all_zero and abs(matrix[i][-1]) > 1e-9:
                print("❌ Sistem tidak konsisten (tidak ada solusi).")
                return None
            elif all_zero and abs(matrix[i][-1]) < 1e-9:
                print("♾️ Sistem memiliki tak hingga solusi.")
                return None
            continue

        # Normalisasi baris i
        pivot = matrix[i][i]
        for j in range(n + 1):
            matrix[i][j] /= pivot

        # Eliminasi kolom i dari baris lain
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

        print(f"Setelah eliminasi kolom {i}:")
        cetak_augmented_matrix(matrix)

    # Ambil solusi dari kolom terakhir
    for i in range(n):
        solusi[i] = matrix[i][n]

    return solusi

def main():
    print("== PROGRAM OPERASI MATRIKS ==")
    print("1. Penjumlahan Matriks")
    print("2. Perkalian Matriks")
    print("3. Sistem Persamaan Linear (Gauss-Jordan Elimination)")
    pilihan = input("Pilih operasi (1/2/3): ").strip()

    if pilihan == "1" or pilihan == "2":
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
    elif pilihan == "3":
        print("\n== INPUT SISTEM PERSAMAAN LINEAR ==")
        matrix, n = input_augmented_matrix()
        solusi = gauss_jordan_elimination(matrix, n)

        if solusi:
            print("== SOLUSI SPL ==")
            for i in range(n):
                print(f"x{i+1} = {solusi[i]:.4f}")
    else:
        print("\n❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
