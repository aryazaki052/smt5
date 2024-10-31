def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b if b != 0 else "Tidak dapat membagi dengan nol"

def pangkat(a, b):
    return a ** b

def kalkulator():
    while True:
        print("\nPilih Operator algoritma yang akan dijalankan:")
        print("1. Operator Penjumlahan")
        print("2. Operator Pengurangan")
        print("3. Operator Perkalian")
        print("4. Operator Pembagian")
        print("5. Operator Pangkat")
        print("99. Keluar")

        pilihan = input("Pilihan kamu? ")

        # Keluar dari program jika memilih 99
        if pilihan == "99":
            print("Program selesai.")
            break

        # Validasi pilihan harus antara 1-5
        if pilihan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan tidak valid, coba lagi.")
            continue

        # Meminta input angka
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid, masukkan angka.")
            continue

        # Menjalankan operasi sesuai pilihan
        if pilihan == "1":
            hasil = penjumlahan(angka1, angka2)
            operasi = "Penjumlahan"
        elif pilihan == "2":
            hasil = pengurangan(angka1, angka2)
            operasi = "Pengurangan"
        elif pilihan == "3":
            hasil = perkalian(angka1, angka2)
            operasi = "Perkalian"
        elif pilihan == "4":
            hasil = pembagian(angka1, angka2)
            operasi = "Pembagian"
        elif pilihan == "5":
            hasil = pangkat(angka1, angka2)
            operasi = "Pangkat"

        print(f"Hasil {operasi} antara {angka1} dan {angka2} adalah: {hasil}")

        # Meminta user apakah ingin melanjutkan atau keluar
        lanjut = input("Apakah ingin melakukan proses lagi? (y/n): ")
        if lanjut.lower() != "y":
            print("Program selesai.")
            break

# Menjalankan program kalkulator
kalkulator()
