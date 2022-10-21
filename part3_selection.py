# nama = input("Masukkan nama: ")
# print("Nama anda ",nama)
# print(f"Nama anda {nama}")

# # PROGRAM MENENTUKAN BILANGAN GANJIL ATAU GENAP

# # mengambil nilai dari user
# x = int(input("Masukkan Bilangan: "))

# # cek nilai apakah genap atau ganjil dengan modulo
# if x % 2 == 0:
#     print(f"Bilangan {x} adalah bilangan genap.")
# else:
#     print(f"Bilangan {x} adalah bilangan ganjil.")



# # inputan dari user
# nilai = int(input("Masukkan nilai: "))
# presensi = int(input("Masukkan presensi: "))

# # cek kondisi cara 1
# if (nilai >= 81) and (presensi>=12):
#     print("Nilai akhir anda A")
# elif (nilai >= 61) and (presensi>=10):
#     print("Nilai akhir anda B")
# elif (nilai >= 41) and (presensi>=8):
#     print("Nilai akhir anda C")
# elif (nilai >= 21) and (presensi>=6):
#     print("Nilai akhir anda D")
# else:
#     print("Nilai akhir anda E")

# # Cara 2
# nilaiHuruf = ''
# if (nilai >= 81) and (presensi>=12):
#     nilaiHuruf = 'A'
# elif (nilai >= 61) and (presensi>=10):
#     nilaiHuruf = 'B'
# elif (nilai >= 41) and (presensi>=8):
#     nilaiHuruf = 'C'
# elif (nilai >= 21) and (presensi>=6):
#     nilaiHuruf = 'D'
# else:
#     nilaiHuruf = 'E'

# print(f'Nilai akhir anda adalah {nilaiHuruf}')

def selectionCar():
    color = input("Warna Mobil: ").lower
    model = int(input("Tahun Model: "))
    mileage = int(input("Jarak Tempuh (km): "))
    car = input("Merek Mobil: ").lower
    decision = ''

    if color=="blue":
        if model>2015:
            decision = 'BELI'
        else:
            if mileage < 500000:
                decision = 'BELI'
            else:
                decision = 'JANGAN BELI'
    elif color=="red" and car=="ferrari":
        decision = 'BELI'
    else:
        decision = 'JANGAN BELI'

    print(f"Saran: {decision} mobil tersebut.")

def selectionHome():
    familyNum = int(input("Jumlah keluarga: "))
    married = input("Status menikah (y/t): ").lower
    salary = int(input("Penghasilan: "))
    decision = ''

    if familyNum > 3:
        if married == 'y':
            decision = '3BHK'
        else:
            if salary > 40000:
                decision = '2BHK'
            else:
                decision = '1BHK'
    else:
        if salary > 80000:
            decision = '4BHK'
        else:
            if married == 'y':
                decision = '3BHK'
            else:
                decision = '2BHK'
    print(f"Anda harus membeli rumah dengan kriteria {decision}")

if __name__ == '__main__':
    selectionHome()