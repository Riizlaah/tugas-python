print("Akar Pangkat Tiga Suatu Bilangan")
num = float(input("Masukkan angka : "))

TOLERANCE = 0.0000001

guess = num / 3
while (guess**3 - num) > TOLERANCE:
  guess = guess - ((guess**3 - num) / (3*guess**2))
print("Akar pangkat tiga dari bilangan", int(num), "adalah %.3f" % guess)