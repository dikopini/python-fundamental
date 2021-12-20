"""
Program perulangan membaca buku dengan while
"""
print("perulangan dengan while")

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang dibaca {jumlah_buku_yang_sudah_dibaca} buku")

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang sudah dibaca sebanyak {jumlah_buku_yang_sudah_dibaca} buku")
