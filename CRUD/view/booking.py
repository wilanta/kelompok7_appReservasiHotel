import datetime
import state
from CRUD.operation.order import booking
from CRUD.utils.clear import clear
from CRUD.utils.messageCountdown import messageNcountdown

def bookingView(hotel):
    from main import main
    error = False
    while True:
        clear()
        if error:
            print("Error saat pengisian!")
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
        total_price = 1

        if check_in_date and check_out_date and total_price and rooms and occupants:
            result, message = booking(check_in_date.strftime(format_date),
                                      check_out_date.strftime(format_date),
                                      rooms, occupants, total_price,
                                      state.USER_ID, hotel['hotel_id'])

            if result:
                messageNcountdown(message)
                main(state.IS_LOGGED_IN, state.USER_LEVEL, state.USERNAME)

        else:
            error = True
