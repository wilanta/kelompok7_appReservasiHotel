import CRUD.view as view
from CRUD.utils.clear import clear

def main():
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
            case "2": view.registerView(0)
            case "3": view.registerView(1)
            case _: print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()