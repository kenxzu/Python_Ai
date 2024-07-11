#Tugas2 asisten dosen AI G
class buku :  

    counter = 0
    def __init__(self, Judul, Author, Harga):
        self.Judul = Judul
        self.Author = Author
        self.Harga = Harga
        buku.counter += 1
    
    def Prifil(self) : 
        print("Nama Buku : ", self.Judul)
        print("Author : ",self.Author)
        print("Harga : ", self.Harga)
        print()

    def Tampilkan_Jumlah(self) : 
         print("Total Buku : ", buku.counter)

Buku1 = buku("Bumi Manusia", "Pramoedya", 5000)
Buku2 = buku("Alchemist ", "Paulo Coeltho", 20000)
Buku3 = buku("Self Power", "Maxwell", 100000)

Buku1.Prifil()
Buku2.Prifil()
Buku3.Prifil()
Buku3.Tampilkan_Jumlah()

 






