import smtplib
import getpass

def emailPenerima():
    jumlah = int(input("Masukkan jumlah email penerima : "))
    def addEmail ():
        file = open ("receiver_list.txt",'a')
        file.write('\n')
        file.write(input("Masukkan email penerima : "))
        file.close()
    for x in range (jumlah):
        addEmail()
    print ('Daftar email : ')
    f = open ("receiver_list.txt",'r')
    print(f.read())

def kirimEmail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()

    # mengirim email
    subject = input("Masukkan Subject email : ")
    body = input("Masukkan Body email : ")
    msg = f'Subject : {subject}\n\n{body}'

    kontak = []
    #untuk memasukan isi file kedalam list
    with open ("receiver_list.txt") as f:
        kontak = f.read().splitlines() 
    
    smtp.login(emailPengirim, passwordEmail)
    smtp.sendmail(emailPengirim,kontak,msg)
    smtp.quit()
    print ("Email berhasil dikirim")


while True :
    print ("----- Final Project -----")
    print ("1. Masukan Email & Password Pengirim")
    print ("2. Masukan Email tujuan")
    print ("3. Kirim Email")
    print ("4. Keluar")
    pilihan = int (input("Masukan pilihan anda : "))

    if pilihan == 1 :
        emailPengirim = input("Masukan email pengirim : ")
        passwordEmail = getpass.getpass("Masukan passowrd email : ")
        print ("Email pengirim berhasil disimpan")
        print("----------")
        print()

    elif pilihan == 2 :
        emailPenerima()
        print("----------")
        print()
    
    elif pilihan == 3 :
        kirimEmail()
        print("----------")
        print()

    elif pilihan == 4 :
        print ("Terima kasih")
        break
    
    else :
        print ("Inputan tidak tersedia")