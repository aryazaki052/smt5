# Meminta input dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
alamat = input("Masukkan Alamat: ")
tahun_angkatan = input("Masukkan Tahun Angkatan: ")

# Membuat nama file berdasarkan NIM yang diinputkan
file_name = f"{nim}.txt"

# Menyimpan data ke file dengan nama file sesuai NIM
with open(file_name, 'w') as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Alamat: {alamat}\n")
    file.write(f"Tahun Angkatan: {tahun_angkatan}\n")

print(f"Data berhasil disimpan di file {file_name}")
