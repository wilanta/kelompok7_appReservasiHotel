# View Module
import CRUD.view as view

import CRUD.operation.hotel as hotel

# State Global Variable
import state

# Utillities Module
from CRUD.utils.clear import clear

def main(isUserLoggedIn=state.IS_LOGGED_IN, userLevel=state.USER_LEVEL, username=state.USERNAME, userId=None):
    # User logged in as visitor
    if isUserLoggedIn and userLevel == "visitor":
        while True:
            clear()

            print(f"SELAMAT DATANG, {username.upper()}!")
            print("BOOKINGHOTEL DOT COM")
            print("===========================")

            # option
            print("1. Cari hotel")
            print("2. Lihat pemesanan")
            print("3. Profile")
            print("0. Keluar")

            user_option = input("\nMasukan opsi : ")

            match user_option:
                case "1": hotel.searchHotels() # fateeh
                case "2": pass # fateeh
                case "3": view.profileView(userId, userLevel)
                case "0": main()
                case _: print("Pilihan tidak valid!")

    # User logged in as admin hotel
    elif isUserLoggedIn and userLevel == "admin":
        while True:
            clear()

            print(f"SELAMAT DATANG, {username.upper()}!")
            print("==== Silakan Kelola Hotel Anda! ====")
            print("BOOKINGHOTEL DOT COM")
            print("===========================")

            # option
            print("1. Kelola Daftar Tamu Hotel")
            print("2. Profile")
            print("0. Keluar")

            user_option = input("\nMasukan opsi : ")

            match user_option:
                case "1": view.manageView(userId, userLevel, username)
                case "2": view.profileView(userId, userLevel)
                case "0": main()
                case _: print("Pilihan tidak valid!")

    # User has been not logged in
    else:
        while True:
            clear()

            print("SELAMAT DATANG DI")
            print("BOOKINGHOTEL DOT COM")
            print("===========================")

            # option
            print("1. Login")
            print("2. Register sebagai pemesan")
            print("3. Register sebagai hotel")

            user_option = input("\nMasukan opsi : ")

            match user_option:
                case "1": view.loginView()
                case "2": view.registerView("visitor")
                case "3": view.registerView("admin")
                case _: print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
