import numpy as np  # type: ignore

def input_matrix(prompt):
    print(f"\n{prompt}")
    rows = int(input("Masukkan jumlah baris: "))
    cols = int(input("Masukkan jumlah kolom: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Masukkan baris ke-{i+1} (pisahkan dengan spasi): ").split()))
        if len(row) != cols:
            raise ValueError("Jumlah elemen tidak sesuai dengan kolom.")
        matrix.append(row)
    return np.array(matrix)

def add_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Dimensi matriks tidak sama untuk penjumlahan.")
    return A + B

def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B untuk perkalian.")
    return np.dot(A, B)

def gauss_jordan_verbose(A_aug):
    A = A_aug.astype(float)
    rows, cols = A.shape
    pivot_row = 0

    print("\n=== PROSES GAUSS-JORDAN ELIMINATION ===")

    for col in range(cols - 1):  # kolom terakhir = konstanta
        print(f"\n>> Mencari pivot di kolom {col}")

        max_row = np.argmax(np.abs(A[pivot_row:, col])) + pivot_row
        print(f"   Pivot terbesar ditemukan di baris {max_row} (nilai = {A[max_row, col]})")

        if A[max_row, col] == 0:
            print(f"   Kolom {col} tidak bisa dijadikan pivot (semua 0)")
            continue

        if max_row != pivot_row:
            print(f"   Menukar baris {pivot_row} dengan baris {max_row}")
            A[[pivot_row, max_row]] = A[[max_row, pivot_row]]
            print(f"   Matriks setelah tukar:\n{np.round(A, 4)}")

        pivot_value = A[pivot_row, col]
        print(f"   Membagi baris {pivot_row} dengan {pivot_value} agar pivot jadi 1")
        A[pivot_row] = A[pivot_row] / pivot_value
        print(f"   Baris {pivot_row} setelah pembagian:\n{np.round(A[pivot_row], 4)}")

        for r in range(rows):
            if r != pivot_row:
                factor = A[r, col]
                print(f"   Eliminasi baris {r}: dikurangi {factor} × baris {pivot_row}")
                A[r] = A[r] - factor * A[pivot_row]
                print(f"   Baris {r} setelah eliminasi:\n{np.round(A[r], 4)}")

        print(f"   Matriks setelah kolom {col} selesai:\n{np.round(A, 4)}")
        pivot_row += 1

    # Deteksi jenis solusi
    solusi = "unik"
    for i in range(rows):
        if all(A[i, :-1] == 0) and A[i, -1] != 0:
            solusi = "tidak ada"
            break
    else:
        rank_A = np.linalg.matrix_rank(A[:, :-1])
        rank_aug = np.linalg.matrix_rank(A)
        if rank_A < rank_aug:
            solusi = "tidak ada"
        elif rank_A < A.shape[1] - 1:
            solusi = "tak hingga"

    print(f"\n=== HASIL AKHIR ===")
    print(f"Matriks RREF:\n{np.round(A, 4)}")
    print(f"Jenis solusi: {solusi.upper()}")
    return A, solusi

def main():
    print("=== Kalkulator Matriks ===")
    while True:
        print("\nMenu:")
        print("1. Penjumlahan Matriks")
        print("2. Perkalian Matriks")
        print("3. Eliminasi Gauss-Jordan (verbose + deteksi solusi)")
        print("4. Keluar")
        pilihan = input("Pilih operasi (1/2/3/4): ")

        if pilihan == '1':
            A = input_matrix("Input Matriks A")
            B = input_matrix("Input Matriks B")
            try:
                result = add_matrices(A, B)
                print("Hasil Penjumlahan:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == '2':
            A = input_matrix("Input Matriks A")
            B = input_matrix("Input Matriks B")
            try:
                result = multiply_matrices(A, B)
                print("Hasil Perkalian:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == '3':
            print("\nEliminasi Gauss-Jordan")
            A_aug = input_matrix("Masukkan matriks augmented (koefisien + hasil kanan)")
            hasil, jenis_solusi = gauss_jordan_verbose(A_aug)

        elif pilihan == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
