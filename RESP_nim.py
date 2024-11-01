rekap_nilai = {
    "Algoritma": {
        "dosen": "Dr. Budiyanto",
        "nilai": [6, 7, 9, 6, 8, 9]
    },
    "Struktur Data": {
        "dosen": "Dr. Erika Nurudin",
        "nilai": [7, 8, 8, 7, 6]
    },
    "Basis Data": {
        "dosen": "Fachrudin, M.Kom.",
        "nilai": [9, 8, 8, 10, 9, 10]
    }
}

def tambah_nilai(nama_mk,nilaiTambahan):
    pesan = ""
    # lanjutkan codingan anda disini
    # percabangan untuk mengecek apakah nama mata kuliah ada dalam dictionary atau tidak
    # jika ada akan menampilkan pesan "Nilai mata kuliah telah ditambahkan"
    # jika tidak akan menampilkan pesan "Mata kuliah tidak ada"
    # ...
    # ...
    return pesan

def hitung_rata_rata(rekap_nilai):
    rerata = {}
    # lanjutkan codingan anda disini
    # gunakan perulangan untuk hitung rata-rata nilai dari setiap mata kuliah yang ada
    # nilai balik berupa dictionary yang berupa nama matakuliah dan nilai rata-ratanya
    # ...
    # ...
    return rerata

print(tambah_nilai("Pancasila",6))
#output: Mata kuliah tidak ada
print(tambah_nilai("Struktur Data",9))
#output: Nilai telah ditambahkan
print(f"Nilai MK Struktur Data: {rekap_nilai['Struktur Data']['nilai']}")
#output: Nilai MK Struktur Data: [7, 8, 8, 7, 6, 9]
print(hitung_rata_rata(rekap_nilai))
#output: {'Algoritma': 7.5, 'Struktur Data': 7.5, 'Basis Data': 9.0}