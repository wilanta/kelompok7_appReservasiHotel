from CRUD.utils.clear import clear
from main import main

def loginView():
    clear()
    print("LOGIN")
    print("[Isi 0 pada isian untuk kembali ke menu]")
    print("===========================")
    
    # Login Form
    email = input("Email\t: ")
    password = input("Password\t: ")
    
    if email == 0 and password == 0:
        main()
    