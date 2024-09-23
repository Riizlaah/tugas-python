import os

fname = input("Masukkan nama depan : ")
lname = input("Masukkan nama belakang : ")
nim = input("Masukkan nim : ")

print("Pendidikan Teknik Informatika".center(os.get_terminal_size().columns))
print("\nNama : {} {}\nNIM : {}\nFakultas Keguruan dan Ilmu Pendidikan\n".format(fname, lname, nim))
print("universitar muhammadiyah surakarta".upper().center(os.get_terminal_size().columns))