#Tahun 2024

while True:
  tahun = input("Masukkan tahun kelahiran : ")
  if tahun.isdecimal(): break
  print("\nTahun kelahiran harus sebuah angka")
while True:
  harga = input("Masukkan harga tiket kereta api : ")
  if harga.isdecimal(): break
  print("\nHarga harus sebuah angka")
harga = int(harga)

umur = 2024 - int(tahun)
diskon = 0

if umur >= 0 and umur <= 4: diskon = 100
if umur >= 5 and umur < 13: diskon = 50
if diskon > 0: print("Mendapat diskon", str(diskon)+"%")

print("Harga :", (harga - int(harga*(diskon/100))))
