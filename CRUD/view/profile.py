# Page Module
from main import main

# Operations Module
from CRUD.operation.auth import searchUser, changeFullname, changeEmail, changePhoneNumber, changePassword, deleteAccount

# Utilities Module
from CRUD.utils.clear import clear

# Main Program
def profileView(userId, userLevel):
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
    
    if userLevel == "visitor":
        print("5. Hapus Akun")
    print("0. Kembali")
    
    user_option = input("\nMasukan opsi : ")

    match user_option:
        case "1": 
            changeFullname(userId)
            profileView(userId, userLevel)
        case "2": 
            changeEmail(userId)
            profileView(userId, userLevel)
        case "3": 
            changePhoneNumber(userId)
            profileView(userId, userLevel)
        case "4": 
            changePassword(userId)
            profileView(userId, userLevel)
        case "5":
            if userLevel == "visitor":
                deleteAccount(userId)
                main()
            else:
                profileView(userId, userLevel)
        case _: print("Pilihan tidak valid!")