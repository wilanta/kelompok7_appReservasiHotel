# Page Module
from main import main

# Operations Module
from CRUD.operation.auth import processLogin

# Utilities Module
from CRUD.utils.clear import clear
from CRUD.utils.messageCountdown import messageNcountdown

# Main Program
def loginView():
    clear()
    print("LOGIN")
    print("[Isi 0 pada isian untuk kembali ke menu]")
    print("===========================")
    
    # Login Form
    email = input("Email\t: ")
    password = input("Password\t: ")
    
    if email == "0" and password == "0":
        main()
    else:
        result, message, username, userLevel = processLogin(email, password)
        
        if result:
            messageNcountdown(message)
            # Redirect to main menu
            if userLevel == "visitor":
                main(True, userLevel, username)
            else:
                main(True, userLevel, username)
        else:
            messageNcountdown(message)
            # Redirect to login
            loginView()