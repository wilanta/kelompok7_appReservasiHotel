# Page Module
from .login import loginView

# Operation Module
from CRUD.operation.hotel import createHotels

# Utilities Module
from CRUD.utils.clear import clear
from CRUD.utils.messageCountdown import messageNcountdown

def registerHotelView(userId):
    clear()
    
    # Title
    print("DAFTARKAN HOTEL ANDA")
    print("===========================")
    
    # Form
    name = input("Nama Hotel\t: ")
    address = input("Alamat Lengkap\t: ")
    city = input("Kota\t: ")
    province = input("Provinsi\t: ")  
    descHotel = input("Deskripsi Hotel\t: ")
    
    # If all filled
    if name and address and city and province:
        result, message = createHotels(
            name,
            address,
            city,
            province,
            descHotel,
            userId
        )
        
        messageNcountdown(message)
        # Redirect to login
        loginView()
    else:
        messageNcountdown("Harap lengkapi data hotel!")
        # Redirect to register hotel
        registerHotelView(userId)
        
    