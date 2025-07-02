import time
import threading
from tabulate import tabulate # type: ignore

# Fungsi versi sekuensial
def hitung_kuadrat_sekuensial():
    hasil = []
    for i in range(1, 1000001):
        hasil.append(i * i)
    return hasil

# Fungsi untuk setiap thread
def hitung_kuadrat(start, end, hasil_local):
    for i in range(start, end):
        hasil_local.append(i * i)

# Fungsi versi multithread
def hitung_kuadrat_multithread():
    threads = []
    hasil_final = [[] for _ in range(4)]
    batas = 1000000 // 4

    for i in range(4):
        awal = i * batas + 1
        akhir = (i + 1) * batas + 1
        t = threading.Thread(target=hitung_kuadrat, args=(awal, akhir, hasil_final[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    hasil = []
    for h in hasil_final:
        hasil.extend(h)
    return hasil

# Hitung waktu eksekusi sekuensial
start_seq = time.time()
hitung_kuadrat_sekuensial()
end_seq = time.time()
waktu_sekuensial = end_seq - start_seq

# Hitung waktu eksekusi multithread
start_mt = time.time()
hitung_kuadrat_multithread()
end_mt = time.time()
waktu_multithread = end_mt - start_mt

# Buat data tabel
data = [
    ["Sekuensial", "1.000.000", "-", f"{waktu_sekuensial:.3f} detik"],
    ["Multithread", "1.000.000", "4", f"{waktu_multithread:.3f} detik"]
]

# Tampilkan tabel
headers = ["Metode", "Jumlah Data", "Jumlah Thread", "Waktu Eksekusi"]
print(tabulate(data, headers=headers, tablefmt="grid"))
