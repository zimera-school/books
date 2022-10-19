the_list = [0, "satu", 2, "tiga", 4]
print(the_list)

the_list.append('lima')
print(the_list)

the_list_01 = [6, 'tujuh', 8]
the_list.extend(the_list_01)
print(the_list)

the_list.insert(4, 'nomor empat')
print(the_list)

the_list.remove('nomor empat')
print(the_list)

the_list_cadangan = []
the_list_cadangan.extend(the_list)
print(the_list_cadangan)
ambil_pop_terakhir = the_list.pop()
print(ambil_pop_terakhir)
print(the_list)
ambil_pop_2 = the_list.pop(2)
print(ambil_pop_2)
print(the_list)

the_list.clear()
print(the_list)

the_list = the_list_cadangan
print(the_list)

print(the_list.index('tujuh'))
print(the_list.index(4,2,6))

the_list.append(4)
print(the_list)
print(the_list.count(4))

#the_list.sort()
#print(the_list)
# TypeError: '<' not supported between instances of 'str' and 'int'
# => hanya bisa sort untuk angka

the_list.reverse()
print(the_list)

# the_list_02 sebenarnya merujuk ke the_list
the_list_02 = the_list
# the_list_shallow akan menghasilkan baru
the_list_shallow = the_list.copy()

# di bawah ini, jika yang clear adalah the_list maka the_list_02 akan ikut
# hilang, sementara the_list_shallow tidak.
print(the_list)
print(the_list_02)
the_list.clear()
print(the_list)
print(the_list_02)
print(the_list_shallow)

the_list = the_list_shallow
print(the_list)

# hapus data pada indeks ke 5 dan 6:
del the_list[5:7]
print(the_list)
