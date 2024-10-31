# nilai1 = input ("masukan angka pertama: ")
# nilai2 = input ("masukan angka kedua: ")

# if int(nilai1) > int(nilai2):
#   print("Nilai pertama yaitu", nilai1, "lebih besar daripada nilai kedua yaitu ", nilai2)
# else:
#   print("Nilai pertama yaitu", nilai1, "lebih keci daripada nilai kedua yaitu ", nilai2)


print("Status kuliah:")
print("1. Online")
print("2. Offline")
print("3. Hybrid")

pilihan = input("Silakan pilih status kuliah Anda (1/2/3): ")

match pilihan:
    case "1":
        print("Status kuliah Anda adalah: Online")
    case "2":
        print("Status kuliah Anda adalah: Offline")
    case "3":
        print("Status kuliah Anda adalah: Hybrid")
    case _:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")
