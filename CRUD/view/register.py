from CRUD.utils.clear import clear
from main import main
from .registerHotel import registerHotelView
from .login import loginView
from CRUD.operation.auth import createRegister

import time

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
    
    # If Password != repassword
    while password != rePassword:
        print("\n\nPASSWORD YANG DIINPUTKAN TIDAK SAMA")
        print("===========================")
        password = input("Password\t: ")
        rePassword = input("Ulangi Password\t: ")
    
    if name == 0 and number == 0 and email == 0 and password == 0 and rePassword == 0:
        main()
    elif userLevel == 0:
        result, message = createRegister(
            name,
            number,
            email,
            password,
            userLevel
        )
        
        if result:
            # Result message
            print(f"{message}\n")
            
            # Countdown
            seconds = 5
            for i in range(seconds, 0, -1):
                print(f"redirect dalam {i}...")
                time.sleep(1)
            
            # Redirect
            loginView()
        else:
            # Result message
            print(f"{message}\n")
            
            # Countdown
            seconds = 5
            for i in range(seconds, 0, -1):
                print(f"redirect dalam {i}...")
                time.sleep(1)
                
            # Redirect
            registerView(userLevel)
            
    elif userLevel == 1:
        result, message = createRegister(
            name,
            number,
            email,
            password,
            userLevel
        )
        
        # Result message
        if result:
            print(message)
            
            # Countdown
            seconds = 5
            for i in range(seconds, 0, -1):
                print(f"redirect dalam {i}...")
                time.sleep(1)
            
            registerHotelView()
        else:
            # Result message
            print(f"{message}\n")
            
            # Countdown
            seconds = 5
            for i in range(seconds, 0, -1):
                print(f"redirect dalam {i}...")
                time.sleep(1)
                
            # Redirect
            registerView(userLevel)