angka1 = input("Masukkan angka pertama: ")              # <1>
angka2 = input("Masukkan angka kedua: ")

if angka1 > angka2:                                     # <2>
  print("Nilai terbesar: ", angka1)                     # <3>
elif angka1 < angka2:
  print("Nilai terbesar: ", angka2)
elif angka1 == angka2:
  print("Kedua angka sama, tidak ada yang terbesar")
else:
  print("Ada masalah dengan angka masukan anda")
