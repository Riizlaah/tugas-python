print("\n", "Konversi Kilometer ke Meter")
while True:
  km = input("Masukkan jarak(kilometer) : ")
  if km.isdecimal(): break
  print("\nMohon masukkan angka yang benar")
km = int(km)
print("Hasil :", km * 1000, "meter")