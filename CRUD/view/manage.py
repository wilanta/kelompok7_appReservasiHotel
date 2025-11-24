# Page Module
from main import main

# Operations Module
from CRUD.operation.manage import showListOrder, updateStatus

# Utilities Module
from CRUD.utils.clear import clear

# Tabulate
import sys
sys.path.append("../lib")
from tabulate import tabulate

# Main Program
def manageView(userId, userLevel, username):
    clear()
    print("KELOLA DAFTAR TAMU HOTEL")
    print("===========================")

    # Get Data
    fetchData = showListOrder(userId)

    # Sorting
    order = {
        "booked": 1,
        "checkin": 2,
        "checkout": 3
    }
    sortedData = sorted(fetchData, key=lambda x: order.get(x["status"], 999))

    # Tambahkan kolom nomor
    numberedData = []
    for i, row in enumerate(sortedData, start=1):
        new_row = {"No": i}
        new_row.update(row)
        numberedData.append(new_row)

    print(tabulate(numberedData, headers="keys", tablefmt="grid"))

    # Option
    print("\n==== Ubah Status CheckIn ====")
    print("1. Pilih nomor")    
    print("0. Kembali")
    
    user_option = input("\nMasukan opsi : ")

    # User chosee 1
    if user_option == "1":
        print("\nPilih nomor booking (1 - {}):".format(len(sortedData)))
        idx = int(input("Nomor : ")) - 1

        if idx < 0 or idx >= len(sortedData):
            manageView(userId, userLevel, username)
        
        selected = sortedData[idx]
        current_status = selected["status"]

        print("\nBooking terpilih:")
        print(f"{selected['fullname']} | {current_status}")

        # Option by status
        if current_status == "booked":
            print('\nTekan ENTER untuk mengubah status ke "checkin"')
            input()
            current_status = "checkin"

        elif current_status == "checkin":
            print('\nTekan ENTER untuk mengubah status ke "checkout"')
            input()
            current_status = "checkout"

        else:
            print("\nStatus sudah 'checkout', tidak bisa diubah lagi.")
            manageView(userId, userLevel, username)

        # Update status
        updateStatus(selected["order_id"], current_status)
        manageView(userId, userLevel, username)
    elif user_option == "0":
        main(True, userLevel, username, userId)
    else:
        manageView(userId, userLevel, username)