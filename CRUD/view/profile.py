# Page Module
# from main import main

# Operations Module
from CRUD.operation.auth import searchUser, changeFullname, changeEmail, changePhoneNumber, changePassword

# Utilities Module
from CRUD.utils.clear import clear

# Main Program
def profileView(userId):
    clear()
    print("PROFILE")
    print("===========================")

    # Get User
    result = searchUser(userId)
    
    # Show Data
    print(f"Nama \t\t: {result['fullname']}")
    print(f"Email \t\t: {result['email']}")
    print(f"Nomor Telepon \t: {result['phone_number']}")
    
    # Option
    print("\n1. Ubah Nama")
    print("2. Ubah Email")
    print("3. Ubah Nomor Telepon")
    print("4. Ubah Password")
    print("0. Kembali")
    
    user_option = input("\nMasukan opsi : ")

    match user_option:
        case "1": 
            changeFullname(userId)
            profileView(userId)
        case "2": changeEmail(userId)
        case "3": changePhoneNumber(userId)
        case "4": changePassword(userId)
        case _: print("Pilihan tidak valid!")