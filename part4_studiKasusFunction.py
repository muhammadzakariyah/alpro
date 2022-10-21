'''
Pada studi kasus ini, modifikasi function yang sudah ada agar program dapat berjalan sebagaimana mestinya.
1. Modifikasi fungsi bernama list_prodi() yang akan mengembalikan list yang berisi:
   "informatika","akuntansi","manajemen"
2. Modifikasi fungsi bernama identitas(...) yang akan menerima 3 argumen berisi nim, nama, prodi yang diinputkan oleh user!
3. Modifikasi fungsi bernama biaya(prodi,jumlah_sks), dan hitung total_biaya berdasarkan biaya spp_variabel dan spp_tetap sesuai prodinya:
   jika prodi informatika, spp_variabel = 200000, spp_tetap = 2500000
   jika prodi akuntansi, spp_variabel = 185000, spp_tetap = 2400000
   jika prodi manajemen, spp_variabel = 170000, spp_tetap = 2300000
   selain ketiga prodi tersebut, spp_variabel = 0, spp_tetap = 0
'''


#1 Modifikasi function ini sehingga memberikan nilai balik berupa list seperti soal nomor 1
def list_prodi():
    ...
    return print(...)

#2 Modifikasi function identitas berdasarkan inputan user
def identitas(...):
    print("Nama ... dengan nim ... dari prodi ...")

#3 Modifikasi function biaya untuk menghitung total_biaya keseluruhan sesuai prodi dan sks yang diinputkan
def biaya(prodi,jumlah_sks):
    spp_variabel = 0
    spp_tetap = 0
    ... # ganti nilai spp_variabel dan spp_tetap
    ... # sesuai dengan prodi yang diinputkan dari user
    ... # (gunakan konsep selection)

    # buat variabel dengan nama total_biaya untuk menghitung total biaya kuliah => (sks*spp_variabel)+spp_tetap
    ...
    return total_biaya


# program utama
if __name__ == '__main__':
    #1 panggil list prodi
    ...

    #2 panggil function identitas dengan argumen nama, nim, dan prodi
    ... # inputan nama
    ... # inputan nim
    prodi = input("Masukkan prodi: ") # inputan prodi
    ... # inputan jumlah_sks
    identitas(...)

    #3 panggil function biaya untuk menghitung biaya kuliah
    biaya_kuliah = biaya(prodi,jumlah_sks)
    print(f"Biaya kuliah saya {...}")