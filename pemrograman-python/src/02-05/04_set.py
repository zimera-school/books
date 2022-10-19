proglang = {'Rust', 'Python', 'Go', 'Rust'}
print(proglang)
tambahan = ('Ruby', 'Lua')
proglang.add(tambahan)
print(proglang)
print('Rust' in proglang)

huruf = set('Zimera Corp.')
print(huruf)

huruf2 = set()
print(huruf2)
huruf2.add('Zimera Corp.')
print(huruf2)

kata1 = set('Indonesia')
kata2 = set('Merdeka')
print(kata1)
print(kata2)

# ada di kata1, tidak ada di kata2
print(kata1 - kata2)

# ada di kata1 atau di kata2 atau di keduanya
print(kata1 | kata2)

# ada di kata1 dan kata2
print(kata1 & kata2)

# ada di kata1 atau di kata2 tapi tidak di keduanya
print(kata1 ^ kata2)
