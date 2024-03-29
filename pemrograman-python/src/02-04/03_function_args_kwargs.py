def penambah(*args):
    total = 0
    for op in args:
        total += op
    return total

jml1 = penambah(1)
jml2 = penambah(23, 24, 21)
jml3 = penambah(1,2,3,4,5,6,7,8,9,10)

print(jml1)
print(jml2)
print(jml3)

list_01 = [3, 5, 9]
list_02 = [11, 51, 20]

# Pada bagian di bawah ini, * digunakan untuk unpack list, yaitu mengambil
# semua isi dari list.
# 3 + 5 +9 + 11 + 51 + 20 = 99
jml4 = penambah(*list_01, *list_02)
print(jml4)

def gabungkan(*args, pemisah='/'):
    return pemisah.join(args)

str_gabung = gabungkan('a','b','c')
str_gabung2 = gabungkan('a','b','c', pemisah='-')

print(str_gabung)
print(str_gabung2)

def get_kwargs(**kwargs):
    return kwargs

def get_key_value(**kwargs):
    for key, value in kwargs.items():
        print("Nilai {} = {}".format(key, value))

kw1 = get_kwargs(product_id='P001', product_name='Laptop')
print(kw1)
get_key_value(product_id='P001', product_name='Laptop')
