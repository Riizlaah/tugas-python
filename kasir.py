import re, datetime, os


barang = {
  'Buku' : 4000,
  'Polpen': 2500,
  'Pensil': 2000,
  'Tipe-x': 5000,
  'Penghapus karet': 1500
}

print("\nSelamat datang di kasir.")
print("List barang :\n1. Buku\n2. Polpen\n3. Pensil\n4. Tipe-x\n5. Penghapus karet")

print("\nMasukkan nomor-nomor barang yang anda beli yang dipisah dengan koma(contoh 1,2,4)")
while True:
  numbers = input("Masukkan sesuai format diatas : ")
  numbers = numbers.replace(" ", "").removeprefix(",").removesuffix(",")
  if(re.search("^[1-5]+(,?[1-5]?,?)", numbers) != None): break
  print("Pola tidak sesuai, masukkan lagi")

arr = numbers.split(",")
arr.reverse()
arr = set(arr)
keys = barang.keys()

barang2 = {}

for i in arr:
  i = int(i) - 1
  nama_barang = list(keys)[i]
  while True:
    jumlah = input("Masukkan jumlah %s : " % nama_barang)
    if jumlah.isdecimal():
      jumlah = int(jumlah)
      if jumlah > 0: break
    print("Jumlah %s haruslah sebuah angka yang lebih besar dari nol" % nama_barang)
  barang2[nama_barang] = {'jumlah': jumlah, 'total-harga': jumlah * barang[nama_barang]}

tw = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

info = "Catatan Pembelian (%s)" % tw
total = 0
for key in barang2.keys():
  info += "\n- %s :\n" % key
  info += "  - jumlah : %s\n" % barang2[key]['jumlah']
  info += "  - harga total barang : %s\n" % barang2[key]['total-harga']
  total += barang2[key]['total-harga']
info += "\nTotal harga semua barang : %s" % total

file = open("catatan_pembelian_"+tw+".txt", "x")
file.write(info)
file.close()

print("\n---\nCatatan Pembelian sudah dibuat, silahkan dilihat\n")