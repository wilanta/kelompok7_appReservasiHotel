from CRUD.utils.clear import clear
from main import main
from .registerHotel import registerHotelView

def registerView(userLevel):
    clear()
    
    # Title
    if userLevel == 0:
        print("REGISTER USER")
    else: 
        print("REGISTER HOTEL")
    print("[Isi 0 pada isian untuk kembali ke menu]")
    print("===========================")
    
    # Form
    name = input("Nama\t: ")
    number = input("Nomor Telepon\t: ")
    email = input("Email\t: ")
    password = input("Password\t: ")
    rePassword = input("Ulangi Password\t: ")
    
    if name == 0 and number == 0 and email == 0 and password == 0 and rePassword == 0:
        main()
    elif userLevel == 1:
        registerHotelView()