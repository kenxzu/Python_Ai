class Kantin:
    def __init__(self):
        self.menu = {}  # Inisialisasi kamus (dictionary) untuk menyimpan daftar menu
        self.total_harga = 0  # Inisialisasi total harga pembelian

    def tambah_menu(self, nama_menu, harga):
        """Fungsi untuk menambahkan menu dan harga ke dalam daftar menu."""
        self.menu[nama_menu] = harga

    def tampilkan_daftar_menu(self):
        """Fungsi untuk menampilkan daftar menu beserta harga."""
        print("Daftar Menu:")
        for menu, harga in self.menu.items():
            print(f"{menu}: Rp{harga}")

    def hitung_total_pembayaran(self, pesanan):
        """Fungsi untuk menghitung total pembayaran berdasarkan pesanan."""
        self.total_harga = 0
        for item in pesanan:
            if item in self.menu:
                self.total_harga += self.menu[item]
            else:
                print(f"Menu '{item}' tidak ada dalam daftar.")
        print(f"Total Pembayaran: Rp{self.total_harga}")

# Contoh penggunaan modul:
if __name__ == "__main__":
    kantin_saya = Kantin()
    
    # Menambahkan menu ke dalam daftar
    kantin_saya.tambah_menu("Nasi Goreng", 15000)
    kantin_saya.tambah_menu("Mie Ayam", 12000)
    kantin_saya.tambah_menu("Es Teh", 5000)
    
    # Menampilkan daftar menu
    kantin_saya.tampilkan_daftar_menu()
    
    # Menghitung total pembayaran
    pesanan = ["Nasi Goreng", "Es Teh", "Ayam Bakar"]
    kantin_saya.hitung_total_pembayaran(pesanan)
