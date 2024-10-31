# latihan 5
# i gusti putu arya zaki yoga pratama 220010117

nilai = int(input("Masukan nilai (1-100): "))

def konversi_nilai(nilai):
    if nilai > 85:
        print("Anda mendapatkan nilai A")
    elif 80 <= nilai <= 85:
        print("Anda mendapatkan nilai AB")
    elif 70 <= nilai < 80:
        print("Anda mendapatkan nilai B")
    elif 65 <= nilai < 70:
        print("Anda mendapatkan nilai BC")
    elif 55 <= nilai < 65:
        print("Anda mendapatkan nilai C")
    elif 40 <= nilai < 55:
        print("Anda mendapatkan nilai D")
    elif 0 <= nilai < 40:
        print("Anda mendapatkan nilai E")
    else:
        print("Nilai di luar rentang 1-100")

konversi_nilai(nilai)
