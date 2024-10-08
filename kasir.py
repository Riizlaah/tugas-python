import re, datetime


barang = {
  'Buku' : 4000,
  'Polpen': 2500,
  'Pensil': 2000,
  'Tipe-x': 5000,
  'Penghapus karet': 1500
}

def unique_arr(arr):
  seen = []
  for x in arr:
    if x not in seen: seen.append(x)
  return seen

print("\nSelamat datang di kasir.")
print("List barang :\n1. Buku : Rp 4000\n2. Polpen : Rp 2500\n3. Pensil : Rp 2000\n4. Tipe-x : Rp 5000\n5. Penghapus karet : Rp 1500")

print("\nMasukkan nomor-nomor barang yang anda beli yang dipisah dengan koma(contoh 1,2,4)")
while True:
  numbers = input("Masukkan sesuai format diatas : ")
  numbers = numbers.replace(" ", "").removeprefix(",").removesuffix(",")
  if(re.search("^[1-5]+(,?[1-5]?,?)", numbers) != None): break
  print("Pola tidak sesuai, masukkan lagi")

arr = numbers.split(",")
arr = unique_arr(arr)
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
tw2 = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

info = "Catatan Pembelian (%s)" % tw2
total = 0
for key in barang2.keys():
  info += "\n- %s :\n" % key
  info += "  - jumlah : %s\n" % barang2[key]['jumlah']
  info += "  - harga total barang : %s\n" % barang2[key]['total-harga']
  total += barang2[key]['total-harga']
info += "\nTotal harga semua barang : %s" % total

namafile = "catatan_pembelian_"+tw+".txt"
file = open(namafile, "x")
file.write(info)
file.close()

print("\n\n-----\n\n"+info+"\n\n-----\n")

print("\nCatatan Pembelian sudah dibuat di dalam file %s, silahkan dilihat\n" % namafile)