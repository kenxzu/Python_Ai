# Import modul "kantin" yang sudah dibuat
from kenmodul import Kantin


def main():
    kantin_saya = Kantin()

    # Menambahkan menu ke dalam daftar
    kantin_saya.tambah_menu("Nasi Goreng", 15000) 
    kantin_saya.tambah_menu("Mie Ayam", 12000)
    kantin_saya.tambah_menu("Es Teh", 5000)

    # Tampilkan daftar menu dari modul
    kantin_saya.tampilkan_daftar_menu()

    # Ambil input user menu dan jumlah pesananan 
    kode_menu = int(input("Masukkan kode menu (1/2/3): ")) 
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

    if kode_menu == 1:
        harga = kantin_saya.menu.get("Nasi Goreng", 0)
    elif kode_menu == 2:
        harga = kantin_saya.menu.get("Mie Ayam", 0)
    elif kode_menu == 3:
        harga = kantin_saya.menu.get("Es Teh", 0)
    else:
        print("Kode menu tidak valid.")
        return

    # Hitung total pembayaran
    total_pembayaran = harga * jumlah_pesanan

    # Menampilkan rincian pesanan dan total
    print(f"Rincian Pesanan:")
    print(f"Menu: {list(kantin_saya.menu.keys())[kode_menu-1]}")
    print(f"Harga per porsi: Rp{harga}")
    print(f"Jumlah pesanan: {jumlah_pesanan}")
    print(f"Total Pembayaran: Rp{total_pembayaran}")

if __name__ == "__main__":
    main()




