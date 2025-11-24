import state
from main import main
from CRUD.operation.order import loadOrders
from CRUD.operation.hotel import loadHotels

def bookingListView():
    orders_data = loadOrders()
    hotels_data = loadHotels()
    hotel_lookup = {hotel['hotel_id']: hotel for hotel in hotels_data}
    orders_list = []
    for order in orders_data:
        hotel_id = order['hotel_id']
        hotel = hotel_lookup.get(hotel_id)

        _order = order.copy()
        _order['hotel_name'] = hotel['name'] if hotel else 'Unknown Name'
        _order['hotel_address'] = hotel['address'] if hotel else 'Unknown Address'

        orders_list.append(_order)

    print("Lihat Daftar Pemesanan")
    print("BOOKINGHOTEL DOT COM")
    print("===========================")

    for index, order in enumerate(orders_list):
        print(f"[{index + 1}.]")
        print(f"Hotel\t\t: {order['hotel_name']}")
        print(f"Alamat\t\t: {order['hotel_address']}")
        print(f"Check-in\t: {order['check_in']}")
        print(f"Check-out\t: {order['check_out']}")
        print(f"Jumlah Kamar \nyang Dipesan\t: {order['room_count']}")
        print(f"Jumlah Orang \nyang Menginap\t: {order['occupants']}")
        print(f"Status\t\t: {order['status']}")
        print("=" * 17)

    while True:
        if input("Back? (Y/T): ").lower() == 'y':
            main(state.IS_LOGGED_IN, state.USER_LEVEL, state.USERNAME)
            break
