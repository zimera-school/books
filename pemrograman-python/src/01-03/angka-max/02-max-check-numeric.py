angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")

if angka1.isnumeric() and angka2.isnumeric():                   # <1>
    if angka1 > angka2:
        print("Nilai terbesar: ", angka1)
    elif angka1 < angka2:
        print("Nilai terbesar: ", angka2)
    elif angka1 == angka2:
        print("Kedua angka sama, tidak ada yang terbesar")
    else:
        print("Ada masalah dengan angka masukan anda")
else:
    print("Anda tidak memasukkan angka")
