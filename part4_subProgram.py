# function tanpa nilai balik dan parameter
def garis():
    print("---------------------")

# function tanpa nilai balik dengan parameter
def tampilIdentitas(nama,nim,prodi):
    print(f"Nama saya {nama} dengan nim {nim}, saya prodi {prodi}")


# function dengan nilai balik tanpa parameter
def operasiAngka():
    bil1 = 100
    bil2 = 60
    hasil = bil1*bil2
    return (bil1,bil2,hasil)

# function dengan nilai balik dan parameter
def operasiAngkaParameter(bil1,bil2):
    return (bil1, bil2, bil1+bil2)

garis()
tampilIdentitas("Zaka","5220411053","Informatika")
a,b,c = operasiAngka()
print(b)

d,e,f = operasiAngkaParameter(4,15)
print(f)