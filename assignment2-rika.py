# Assigment-2 Rika

Daftar_kontak = {}
def inputKontak () :
    namaKontak = input('Masukan Nama: ')
    nomorKontak = input('Masukan No. Telepon: ')
    Daftar_kontak[namaKontak] = nomorKontak
    print ('Kontak berhasil ditambahakan')

def showKontak () :
    print ('Daftar Kontak')
    for i,j in Daftar_kontak.items () :
        print ('Nama: '+i)
        print ('Nomor Telepon: ' +j)
        print ('------------------------------')

while True:
   print('''
   Selamat Datang !
   -- Menu --
   1. Daftar Kontak
   2. Tambah Kontak
   3. Keluar
   ''')
   pilihan = int(input('Pilih menu: '))
   
   if pilihan == 1:
      showKontak()
      print ()

   elif pilihan == 2:
      inputKontak()
      print ()

   elif pilihan == 3:
        print('Program selesai, sampai jumpa!')
        break

   else :
      print('Menu tidak tersedia')