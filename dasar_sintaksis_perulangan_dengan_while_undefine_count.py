"""
Program perulangan membaca buku dengan while
"""
print("perulangan dengan while")

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0
print(f"jumlah buku yang dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print (f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah dibaca dan dipahami sebanyak {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku")

if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, semua buku bisa dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku"')