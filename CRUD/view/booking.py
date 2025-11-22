import datetime
import state
from CRUD.utils.clear import clear

def bookingView(hotel):
    from main import main
    clear()
    print(f"Pesan Kamar di {hotel['name']}")
    print("[Isi \"exit\" pada isian untuk kembali ke menu]")
    check_in    = input("Waktu Check-in (YYYY-MM-DD) : ")
    if check_in.lower().strip() == "exit":
        main(state.IS_LOGGED_IN, state.USER_LEVEL, state.USERNAME)

    check_out   = input("Waktu Check-out (YYYY-MM-DD): ")
    rooms       = input("Kamar yang dipesan\t : ")
    occupants   = input("Orang yang bertamu\t : ")

    format_date = "%Y-%m-%d"
    check_in_date = datetime.datetime.strptime(check_in, format_date)
    check_out_date = datetime.datetime.strptime(check_out, format_date)
    total_price = 0
    status = "pending"