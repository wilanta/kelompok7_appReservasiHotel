from CRUD.utils.clear import clear

import datetime

def bookingView(hotel):
    clear()
    print(f"Pesan Kamar di {hotel['name']}")
    print("[Isi \"exit\" pada isian untuk kembali ke menu]")
    check_in    = input("Waktu Check-in (YYYY-MM-DD): ")
    check_out   = input("Waktu Check-in (YYYY-MM-DD): ")
    check_in    = input("Kamar yang dipesan\t: ")
    check_out   = input("Orang yang bertamu\t: ")

    format_date = "%Y-%m-%d"
    check_in_date = datetime.datetime.strptime(check_in, format_date)
    check_out_date = datetime.datetime.strptime(check_out, format_date)

