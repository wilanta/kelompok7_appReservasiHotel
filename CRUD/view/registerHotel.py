from CRUD.utils.clear import clear
from .login import loginView 

def registerHotelView():
    clear()
    
    # Title
    print("DAFTARKAN HOTEL ANDA")
    print("===========================")
    
    # Form
    name = input("Nama Hotel\t: ")
    address = input("Alamat Lengkap\t: ")
    city = input("Kota\t: ")
    state = input("Provinsi\t: ")    
    
    if name and address and city and state:
        loginView()
    