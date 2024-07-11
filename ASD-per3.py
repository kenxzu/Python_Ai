class Karyawan :
    jumlah_karyawan = 0

    def __init__(self, name, umur) :
        self.name = name
        self.umur = umur

        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print(" Total ", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self) :
        print("nama ", self.name)
        print("age " , self.umur)
        print()

karyawan1 = Karyawan("ken", 12)
karyawan2 = Karyawan("jan", 12)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()

# print(Karyawan.jumlah_karyawan)