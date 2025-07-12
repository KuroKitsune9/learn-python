import numpy as np # type: ignore

def input_matriks(nama, baris = 0, kolom = 0):
    if baris == 0 and kolom == 0:
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

    return np.array(matriks)

def penjumlahan_matriks():
    print("-- PENJUMLAHAN MATRIKS --")
    A = input_matriks("A")
    B = input_matriks("B")

    # Mengecek apakah ukuran matriks A dan B sama
    if A.shape != B.shape:
        print("Matriks A dan B harus memiliki ukuran yang sama untuk dijumlahkan.")
        return

    hasil = A + B
    print("Hasil Penjumlahan Matriks A dan B:")
    print(hasil)

def pengurangan_matriks():
    print("-- PENGURANGAN MATRIKS --")
    A = input_matriks("A")
    B = input_matriks("B")

    # Mengecek apakah ukuran matriks A dan B sama
    if A.shape != B.shape:
        print("Matriks A dan B harus memiliki ukuran yang sama untuk dijumlahkan.")
        return

    hasil = A - B
    print("Hasil Pengurangan Matriks A dan B:")
    print(hasil)

def perkalian_matriks():
    print("-- PERKALIAN MATRIKS --")
    A = input_matriks("A")
    B = input_matriks("B")

    # Mengecek apakah jumlah kolom matriks A sama dengan jumlah baris matriks B
    if A.shape[1] != B.shape[0]:
        print("Perkalian tidak dapat dilakukan: jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B.")
        return

    # Perkalian Matriks
    hasil = np.dot(A, B)
    print("Hasil Perkalian Matriks A dan B:")
    print(hasil)

def pembagian_matriks():
    print("-- PEMBAGIAN MATRIKS --")
    
    # Input matriks A dan B
    A = input_matriks("A")
    B = input_matriks("B")

    # Mengecek apakah matriks B dapat diinversikan
    if np.linalg.det(B) == 0:
        print("Matriks B tidak dapat diinversikan karena determinannya nol.")
        return

    # Menghitung invers dari matriks B
    B_inv = np.linalg.inv(B)

    # Melakukan pembagian (A * B^-1)
    hasil = np.dot(A, B_inv)
    print("Hasil Pembagian Matriks A dan B:")
    print(hasil)

def operasi_matriks():
    print("-- OPERASI MATRIKS --")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Pembagian Matriks")
    pilihan = input("Masukan Pilihan: ").strip()
    if pilihan == '1':
        penjumlahan_matriks()
    elif pilihan == '2':
        pengurangan_matriks()
    elif pilihan == '3':
        perkalian_matriks()
    elif pilihan == '4':
        pembagian_matriks()
    else:
        print("Pilihan tidak tersedia.")

def gauss_jordan():
    print("-- METODE GAUSS JORDAN --")

    A = input_matriks("Koefisien")
    b = input_matriks("Konstanta", A.shape[0], 1)

    # Gabungkan jadi augmented matrix dan ubah ke float agar pembagian bisa dilakukan
    augmented_matrix = np.hstack((A.astype(float), b.astype(float)))
    rows, cols = augmented_matrix.shape

    for i in range(rows):
        # Tangani pivot 0 dengan tukar baris
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, rows):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
            else:
                print("Pivot 0 tidak dapat diatasi, sistem mungkin tidak memiliki solusi unik.")
                return

        # Normalisasi baris (pivot jadi 1)
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

        # Eliminasi elemen selain pivot di kolom yang sama
        for j in range(rows):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

    solusi = augmented_matrix[:, -1]
    print("Solusi dari sistem persamaan adalah:")
    print(solusi)

def main():
    print("== PROGRAM KALKULATOR MATRIKS ==")
    print("1. Operasi Matrix")
    print("2. Metode Gauss Jordan")
    pilihan = input("Masukan Pilihan: ").strip()
    if pilihan == '1':
        operasi_matriks()
    elif pilihan == '2':
        gauss_jordan()
    else:
        print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()