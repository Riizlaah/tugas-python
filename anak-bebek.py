
while True:
  jumlah = input("Masukkan jumlah anak bebek : ")
  if jumlah.isdecimal(): break
  print("\nJumlah haruslah angka")

i = int(jumlah)

while i > 0:
  line = "Anak bebek turun %d, mati satu tinggal " % i
  i -= 1
  if i > 0: line += str(i)
  else: line += "induknya"
  print(line)