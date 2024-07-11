import random

def generate_soal():
    # generate 2 angka secara random
    angka1 = random.randint(1, 10)
    angka2 = random.randint(1, 10)
    
    # gabungkan angka untuk membuat soal
    soal = f"Berapakah hasil dari {angka1} x {angka2}?"
    
    # hitung jawaban yang benar
    jawaban_benar = angka1 * angka2
    
    return soal, jawaban_benar

def main():
    # generate soal pertama
    soal, jawaban_benar = generate_soal()
    
    # tampilkan soal dan minta input dari pengguna
    while True:
        print(soal)
        jawaban = input("Jawaban: ")
        
        # cek jawaban
        if jawaban.isdigit() and int(jawaban) == jawaban_benar:
            print("Benar")
            break
        else:
            print("Salah, coba lagi")

if __name__ == '__main__':
    main()