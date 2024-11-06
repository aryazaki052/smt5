# Membuka dan membaca isi file 220010117.txt
with open('220010117.txt', 'r') as file:
    lines = file.readlines()  # Membaca semua baris di file 220010117.txt

# Menghapus baris kosong dan memilih baris genap, dimulai dari baris pertama (dihitung dari 1)
even_lines = [line.strip() for i, line in enumerate(lines, start=1) if i % 2 == 0 and line.strip()]

# Menuliskan hasil baris genap ke dalam file baru output.txt
with open('output.txt', 'w') as output_file:
    for line in even_lines:
        output_file.write(line + '\n')  # Menulis tiap baris ke file output.txt, ditambah newline
