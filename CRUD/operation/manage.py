# Libraries
import json
import os

# Import for Fetch
from CRUD.operation.auth import loadUsers
from CRUD.operation.hotel import loadHotels

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "orders.json")
DATA_FILE = os.path.abspath(DATA_FILE)

# Helper
def loadOrders():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def saveOrders(orders):
    with open(DATA_FILE, "w") as f:
        json.dump(orders, f, indent=4)

# Show list order
def showListOrder(userId):
    users = loadUsers()
    orders = loadOrders()
    hotels = loadHotels()

    # Mapping user_id to user
    userMap = {u["user_id"]: u for u in users}

    # Search hotel admin
    adminHotel = None
    for h in hotels:
        if h["user_id"] == userId:
            adminHotel = h
            break

    adminHotelId = adminHotel["hotel_id"]

    # Filter orders for the admin only
    result = []
    for order in orders:
        if order["hotel_id"] != adminHotelId:
            continue

        # Get user data
        user = userMap.get(order["user_id"])
        if not user:
            continue

        # Append needed data
        result.append({
            "order_id": order["order_id"],
            "user_id": user["user_id"],
            "fullname": user["fullname"],
            "check_in": order["check_in"],
            "check_out": order["check_out"],
            "room_count": order["room_count"],
            "occupants": order["occupants"],
            "price": order["price"],
            "status": order["status"],
        })

    return result

# Update Order Status
def updateStatus(orderId, newStatus):
    orders = loadOrders()
    for order in orders:
        if order["order_id"] == orderId:
            order['status'] = newStatus
            saveOrders(orders)
            break