"""
Program perulangan membaca buku dengan for
"""
print("perulangan dengan for")

jumlah_buku = 50
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang dibaca {jumlah_buku_yang_sudah_dibaca} buku")

for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang dibaca {jumlah_buku_yang_sudah_dibaca} buku")