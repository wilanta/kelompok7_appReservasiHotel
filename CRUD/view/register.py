# Pages Module
from main import main
from .registerHotel import registerHotelView
from .login import loginView

# Operation Module
from CRUD.operation.auth import createRegister

# Utilities Module
from CRUD.utils.clear import clear
from CRUD.utils.randomId import idRandom
from CRUD.utils.messageCountdown import messageNcountdown

# Main Program
def registerView(userLevel):
    clear()

    # Title
    if userLevel == "visitor":
        print("REGISTER USER")
    else:
        print("REGISTER HOTEL")
    print("[Isi \"exit\" pada isian untuk kembali ke menu]")
    print("===========================")

    # Form
    userId = idRandom()
    name = input("Nama\t\t: ")

    # Move to previous page
    if name.lower().strip() == "exit":
        main()

    number = input("Nomor Telepon\t: ")
    email = input("Email\t\t: ")
    password = input("Password\t: ")
    rePassword = input("Ulangi Password\t: ")

    # If Password != repassword
    while password != rePassword:
        print("\n\nPASSWORD YANG DIINPUTKAN TIDAK SAMA")
        print("===========================")
        password = input("Password\t: ")
        rePassword = input("Ulangi Password\t: ")

    # Empty input
    if name == "" or number == "" or password == "":
        messageNcountdown("Harap masukkan data anda dengan lengkap!")
        # Redirect to register user
        registerView(userLevel)

    # Level user : hotel visitor
    elif userLevel == "visitor":
        result, message = createRegister(
            userId,
            name,
            number,
            email,
            password,
            userLevel
        )

        if result:
            messageNcountdown(message)
            # Redirect to login
            loginView()
        else:
            messageNcountdown(message)
            # Redirect to register user
            registerView(userLevel)

    # Level user : hotel admin
    elif userLevel == "admin":
        result, message = createRegister(
            userId,
            name,
            number,
            email,
            password,
            userLevel
        )

        # Result message
        if result:
            messageNcountdown(message)
            # Redirect to register hotel
            registerHotelView(userId)
        else:
            messageNcountdown(message)
            # Redirect to register user
            registerView(userLevel)
