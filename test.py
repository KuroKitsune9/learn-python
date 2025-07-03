import time
import threading
import matplotlib.pyplot as plt # type: ignore

# Fungsi versi sekuensial
def hitung_kuadrat_sekuensial():
    hasil = []
    for i in range(1, 1000001):
        hasil.append(i * i)
    return hasil

# Fungsi untuk tiap thread
def hitung_kuadrat(start, end, hasil_local):
    for i in range(start, end):
        hasil_local.append(i * i)

# Fungsi versi multithreading
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

# Eksekusi versi sekuensial
start_seq = time.time()
hitung_kuadrat_sekuensial()
end_seq = time.time()
waktu_sekuensial = end_seq - start_seq

# Eksekusi versi multithreading
start_mt = time.time()
hitung_kuadrat_multithread()
end_mt = time.time()
waktu_multithread = end_mt - start_mt

# Data untuk grafik
versi = ['Sekuensial', 'Multithread']
waktu = [waktu_sekuensial, waktu_multithread]

# Buat grafik perbandingan
plt.bar(versi, waktu, color=['blue', 'green'])
plt.ylabel("Waktu (detik)")
plt.title("Perbandingan Waktu Eksekusi Program", pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan nilai di atas batang
for i in range(len(waktu)):
    plt.text(i, waktu[i] + 0.005, f"{waktu[i]:.3f}", ha='center')

plt.tight_layout()
plt.show()
