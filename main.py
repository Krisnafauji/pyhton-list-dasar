from program.Inputnilai import inputnilai
from program.Penggajian import penggajian
from program.calculator import calculator
from program.pembayaran import pembayaran


def menu() :
    
    print("MENU UTAMA")
    print("\t 1. PENILAIAN MAHASISWA ")
    print("\t 2. GAJI KARYAWAN ")
    print("\t 3. PEMBAYARAN MAHASISWA ")
    print("\t 4. PROGRAM KALKULATOR SEDERHANA ")
    print("\t 5. EXIT")
    pilihan = input("\nMasukkan Pilihan ( 1 \ 2 \ 3 \ 4 \ 5) ? ")
    if pilihan == '1' :
        inputnilai()
    elif pilihan == '2' :
        penggajian()
    elif pilihan == '3' :
        pembayaran()
    elif pilihan == '4' :
        calculator ()
    elif pilihan == '5' :
        print("TERIMA KASIH")
    else :
        print("\nPILIHAN TIDAK DITEMUKAN!!")
    tambahan()
    
   

def tambahan() :
    
    tanya = input("\t\nKembali ke MENU UTAMA : ")
    if tanya == "y" :
        menu()
    elif tanya == "t" :
        print("Terima Kasih")
    else :
        print("salah input")
        exit

print("Silahkan Anda Login")       
nama = "krisna fauji"
kunci = "130800"
lagi = 'y'
a = 0
while lagi == 'y' :
    username = input("Masukkan Username Anda : ")
    import getpass
    password = getpass.getpass()
    if(username == nama and password == kunci) :
        print("Anda Telah Login")
        break
       
    elif (username == nama or password == kunci) :
        print("username atau password anda salah")
    else :
        print("Password Salah")
    a=a+1
    if a==3 :
        print("sudah 3x input")
        break
        
    print()
    lagi = input("Input kembali, y / t?  ")
    print()
        
menu()

     
