def apakah_prima(b):
  b = int(b)
  if b <= 1:
    print(str(b)+" bukan bilangan prima")
    return
  n = 0
  for i in range(1, b + 1):
    if b % i == 0: n += 1
  if n == 2:
    print(str(b)+" adalah bilangan prima")
    return
  print(str(b)+" bukan bilangan prima")


while True:
  bil = input("Masukkan bilangan : ")
  if bil.isdecimal(): break
  print("\nbilangan haruslah angka")

apakah_prima(bil)