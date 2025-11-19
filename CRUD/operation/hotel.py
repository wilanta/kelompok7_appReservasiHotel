from CRUD.utils.randomId import idRandom

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "hotels.json")
DATA_FILE = os.path.abspath(DATA_FILE)

# Helper
def loadHotels():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def saveHotels(hotels):
    with open(DATA_FILE, "w") as f:
        json.dump(hotels, f, indent=4)

# Register Process
def createHotels(name, address, city, province, descHotel, userId):
    hotels = loadHotels()

    hotel = {
        "hotel_id": idRandom(),
        "name": name.lower(),
        "address": address.lower(),
        "city": city.lower(),
        "province": province.lower(),
        "desc_hotel": descHotel.lower(),
        "overall_rating": 0,
        "user_id": userId
    }

    hotels.append(hotel)
    saveHotels(hotels)
    return True, "Hotel berhasil disimpan!"