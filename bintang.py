def pola_bintang_berulang(baris, pengulangan):
    for ulang in range(pengulangan):
        # Segitiga naik
        for i in range(1, baris + 1):
            print('*' * i)
        # Segitiga turun
        for i in range(baris - 1, 0, -1):
            print('*' * i)
        print()  # spasi antar pengulangan

# Contoh penggunaan
pola_bintang_berulang(baris=3, pengulangan=1)
