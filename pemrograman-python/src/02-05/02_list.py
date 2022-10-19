the_list = [0, "satu", 2, "tiga", 4]

print(the_list)
print()

the_list.append('lima')

print(the_list)
print()

the_list_01 = [6, 'tujuh', 8]
the_list.extend(the_list_01)

print(the_list)
print()

the_list.insert(4, 'nomor empat')

print(the_list)
print()

the_list.remove('nomor empat')

print(the_list)
print()

the_list_cadangan = the_list

print(the_list_cadangan)
print()

ambil_pop_terakhir = the_list.pop()
print(ambil_pop_terakhir)
print(the_list)
print()

ambil_pop_2 = the_list.pop(2)
print(ambil_pop_2)
print(the_list)
print()

the_list.clear()
print(the_list)
print()

the_list = []
the_list.extend(the_list_cadangan)
print(the_list)
print()

print(the_list.index('tujuh'))






















