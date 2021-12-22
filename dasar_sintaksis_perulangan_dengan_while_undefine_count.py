"""
Program perulangan membaca buku dengan while
"""
print("perulangan dengan while")

buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_paham = 0
total_jumlah_baca = 0
print(f"jumlah buku yang dibaca dan dipahami {jumlah_paham} buku")

while total_jumlah_baca < buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_paham == 9:
        print (f"Buku ke {jumlah_paham + 1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah dibaca dan dipahami sebanyak {jumlah_paham} buku")

if jumlah_paham == buku:
    print('"Bu, semua buku bisa dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_paham} buku"')