def jumlah(arg1):                                                       # <1>
    jml = 0                                                             # <2>
    for a in arg1:
        jml += 1
    return jml                                                          # <3>

str_obj_1 = "Zimera Corporation"                                        # <4>
str_obj_2 = "Zimera School"
str_obj_3 = "Zimera Systems"

jml_str_1 = jumlah(str_obj_1)                                           # <5>
jml_str_2 = jumlah(str_obj_2)                                           # <6>
jml_str_3 = jumlah(str_obj_3)                                           # <7>

print(f'String {str_obj_1} mempunyai ' + str(jml_str_1) + ' karakter')
print(f'String {str_obj_2} mempunyai ' + str(jml_str_2) + ' karakter')
print(f'String {str_obj_3} mempunyai ' + str(jml_str_3) + ' karakter')
