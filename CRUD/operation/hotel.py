from CRUD.utils.randomId import idRandom
from CRUD.view.booking import bookingView
from CRUD.utils.clear import clear

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "hotels.json")
DATA_FILE = os.path.abspath(DATA_FILE)

# Helper
def loadHotels():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def saveHotels(hotels):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(hotels, f, indent=4)

# Register Process
def createHotels(name, address, city, province, descHotel, price, roomAvailable, userId):
    hotels = loadHotels()

    hotel = {
        "hotel_id": idRandom(),
        "name": name.lower(),
        "address": address.lower(),
        "city": city.lower(),
        "province": province.lower(),
        "desc_hotel": descHotel.lower(),
        "price": price,
        "room_available": roomAvailable,
        "overall_rating": 0,
        "user_id": userId
    }

    hotels.append(hotel)
    saveHotels(hotels)
    return True, "Hotel berhasil disimpan!"

def searchHotels(dataHotel = None):
    if dataHotel is None:
        dataHotel = loadHotels()

    while True:
        query = input("Masukkan nama atau lokasi hotel: ").lower()

        hasil = []
        for hotel in dataHotel:
            if query in hotel['city'].lower() or query in hotel['name'].lower():
                hasil.append(hotel)

        if len(hasil) > 0:
            print("===== HASIL =====")
            for index, result in enumerate(hasil):
                print(f"[{index + 1}.]")
                print(f"Nama\t\t: {result['name']}")
                print(f"Alamat\t\t: {result['address']}")
                print(f"Kota\t\t: {result['city']}")
                print(f"Provinsi\t: {result['province']}")
                print(f"Ulasan\t\t: {result['overall_rating']}")
                print(f"Deskripsi\t: {result['desc_hotel']}")
                print("=" * 17)
        else:
            print("Hotel tidak ditemukan!")

        select = input("Pilih nomor hotel atau Cari lagi (ketik 0): ")

        if select.isdigit() and int(select) == 0:
            break

        if select.isdigit() and int(select) > 0:
            try:
                if int(select) - 1 <= len(hasil):
                    bookingView(hasil[int(select)-1])
                    break
            except IndexError:
                print("Error: Masukkan nilai yang sesuai!")
