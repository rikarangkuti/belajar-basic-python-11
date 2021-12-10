# Soal no 1
Nama = input("Masukan Nama Anda: ")
Umur = int(input("Masukan Umur Anda: "))
Tinggi = float(input("Masukan Tinggi Anda: "))

print("Nama saya {}, umur {}, tinggi {}".format(Nama,Umur,Tinggi))

# Soal no 2
phi = 22/7
r = float(input("Masukan nilai r : "))
L = phi*(r**2)
print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,L))

# Soal no 3

nilai_teori = float(input("Masukan nilai teori : "))
nilai_praktek = float(input("Masukan nilai praktek : "))

if nilai_teori >= 70 and nilai_praktek >= 70 :
    print("Selamat, anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70 :
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori <= 70 and nilai_praktek >= 70 :
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")

