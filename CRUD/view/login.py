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
    print("[Isi \"exit\" pada isian untuk kembali ke menu]")
    print("===========================")

    # Login Form
    email = input("Email\t\t: ")
    if email.lower().strip() == "exit":
        main()
    
    password = input("Password\t: ")

    result, message, username, userId, userLevel = processLogin(email, password)
    if result:
        messageNcountdown(message)
        # Redirect to main menu
        if userLevel == "visitor":
            main(True, userLevel, username, userId)
        else:
            main(True, userLevel, username, userId)
    else:
        messageNcountdown(message)
        # Redirect to login
        loginView()
