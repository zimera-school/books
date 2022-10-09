## Base 2 - Biner

# print(0b12)
# error:     
# print(0b12)
#          ^
# SyntaxError: invalid syntax

print(0b1101)
# Hasil:
# 13
# (1101) basis biner = (1 x 2^3) + (1 x 2^2( + (0 x 2^1) + (1 x 2^0) = (13) basis 10

## Base 8 - Octal

print(0o10) #  0 dan huruf o
# Hasil:
# 8
# (10) basis 8 = (1 x 8^1) + (0 x 8^0) = (8) basis 10

## Base 16 - Hexadecimal

print(0x1AB)
# Hasil:
# 427
# (1AB) basis 16 = (1 x 16^2) + (10 x 16^1) + (10 x 16^0) = (427) basis 10

print(type(0b1101))
print(type(0o10))
print(type(0x1AB))

# Hasil: semua akan dianggap Integer
# <type 'int'>
# <type 'int'>
# <type 'int'>
