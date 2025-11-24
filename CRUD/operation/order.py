from CRUD.utils.randomId import idRandom

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "orders.json")
DATA_FILE = os.path.abspath(DATA_FILE)

def loadOrders():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def saveOrders(orders):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4)

# Register Process
def booking(check_in, check_out, room_count, occupants, price, userId, hotelId, rating = 0):
    orders = loadOrders()

    order = {
        "order_id": idRandom(),
        "hotel_id": hotelId,
        "user_id": userId,
        "check_in": check_in,
        "check_out": check_out,
        "room_count": room_count,
        "occupants": occupants,
        "price": price,
        "rating": rating,
        "status": "booked",
    }

    orders.append(order)
    saveOrders(orders)
    return True, "Pemesanan telah berhasil!"
