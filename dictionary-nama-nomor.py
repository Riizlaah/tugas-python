
data = {}

for i in range(5):
  nama = input("\nMasukkan nama : ")
  no = input("Masukkan nomor telepon : ")
  data[nama] = no
print("\n")
for key in data.keys():
  print(key, "=", data[key])