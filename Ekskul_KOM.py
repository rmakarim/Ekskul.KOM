# VARIABLE

nama = "Karim" # string
umur = 15 # integer
lakilaki = True # boolean (True/False)

daftarNama = ["Raffa", "Abhinaya", "Makarim"] # array

kalimat = "Nama saya " + nama +". Umur saya " + str(umur) + "tahun" # type casting
# Nama saya Karim. Umur saya 15 tahun

if not lakilaki:
    print("saya perempuan")
else:
    print("saya laki-laki")

print(nama)
nama=15

panjang = len(daftarNama) 
# isi dari array jumlahnya berapa

daftarNama.append("Tambahan")
# daftar nama = ["Raffa", "Abhinaya", "Makarim"]

print(daftarNama[3])

# FUNCTION
# function name
# function body
# paremeter (0=< N)
# return value (0=< N)
def tambah(a, b):
    hasil = a + b
    return hasil

c = tambah(5, 4)
print("hasil adalah "+ str(c))

# PERCABANGAN
# IF
n = 9
if n < 10:
    print("n adalah satuan")

# if else
b = 10
if b < 10 and n> 0: 
    print("n adalah satuan" + str(n))
else:
    print("n bukan satuan")
# if else if
b = 10
if b < 0:
    print("b bukan negatif b adalah " + str(b))
elif b < 10:
    print("b adalah satuan")
else:
    print("b lebih dari atau sama dengan 10")

# PERULANGAN
# literasi
# for loop
i = 0
for nama in daftarNama:
    # nama = daftarNama[index]
    i += 1 # i + 1 
    print(str(i) + "==" + nama)
    # i += 1
    
    
