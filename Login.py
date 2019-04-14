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
