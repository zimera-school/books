# definisi kelas paling sederhana
# bisa ditambah properties
class Dosen:
    pass

bpdp = Dosen()
bpdp.nama = 'Bambang Purnomosidi'

print(bpdp)
print(bpdp.nama)

class DosenUTDI(Dosen):

    institusi = 'Universitas Teknologi Digital Indonesia'

    # konstruktor
    def __init__(self, npp, nama):
        self.npp = npp
        self.nama = nama

    def mengajar(self, *args):
        self.mk_diampu = args

bambangpdp = DosenUTDI('123', 'Bambang Purnomosidi D. P.')
print(bambangpdp)
bambangpdp.mengajar('Teknologi Cloud Computing', 'Big Data Analytics')
print(bambangpdp.mk_diampu)
print(bambangpdp.institusi)

class DosenUTDIMTI(DosenUTDI):

    prodi = 'Magister Teknologi Informasi'

zaky = DosenUTDIMTI('213','Zaky')
print(zaky.institusi)
print(zaky.prodi)
