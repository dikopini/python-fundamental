"""
Semua sintaksis bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, " Apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu. jika ada telor, beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

#Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1586
print(f"jumlah botol susu {jumlah_botol_susu} btl")
print(f"jumlah telur {jumlah_telur} tlr")

if jumlah_botol_susu > 0:
    print("BUdi mengecek harga dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu")
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")