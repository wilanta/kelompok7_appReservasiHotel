# Libraries
import json
import os
import state

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")
DATA_FILE = os.path.abspath(DATA_FILE)

# Helper
def loadUsers():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def saveUsers(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def emailExists(email, users):
    return any(u["email"] == email for u in users)


# Register Process
def createRegister(userId, name, number, email, password, userLevel):
    users = loadUsers()

    if emailExists(email, users):
        return False, "Email sudah terdaftar!"

    user = {
        "user_id": userId,
        "fullname": name.lower(),
        "phone_number": number,
        "email": email,
        "password": password,
        "user_level": userLevel
    }

    users.append(user)
    saveUsers(users)
    return True, "Pendaftaran berhasil!"


# Login Process
def processLogin(email, password):
    users = loadUsers()

    for user in users:
        if user["email"] == email and user["password"] == password:
            state.USER_ID = user['user_id']
            return True, f"Login berhasil! Selamat datang, {user['fullname'].title()}", user['fullname'], user['user_id'], user['user_level']

    return False, "Email atau password salah!", "", "", ""

# Search User
def searchUser(userId):
    users = loadUsers()
    
    for user in users:
        if user["user_id"] == userId:
            return user
    return None

# Change User Fullname
def changeFullname(userId):
    # Get New Name
    newName = input("\nMasukan nama baru : ")
        
    # Get Target ID and Change Name
    users = loadUsers()
    for user in users:
        if user["user_id"] == userId:
            user['fullname'] = newName
            saveUsers(users)
            break

# Change User Email
def changeEmail(userId):
    # Get New Email
    newMail = input("\nMasukan email baru : ")
        
    # Get Target ID and Change Email
    users = loadUsers()
    for user in users:
        if user["user_id"] == userId:
            user['email'] = newMail
            saveUsers(users)
            break

# Change User Phone Number
def changePhoneNumber(userId):
    # Get New Number
    newNumber = input("\nMasukan nomor telepon baru : ")
        
    # Get Target ID and Change Number
    users = loadUsers()
    for user in users:
        if user["user_id"] == userId:
            user['phone_number'] = newNumber
            saveUsers(users)
            break

# Change User Password
def changePassword(userId):
    while True:
        password = input("\nMasukan password lama : ")
        
        # Load User Data
        users = loadUsers()
        for user in users:
            # Validate User
            if user["user_id"] == userId and user["password"] == password:
                print("\n==== Buat Password Baru ====")
                newPassword = input("Password Baru \t\t: ")
                newRePassword = input("Ulangi Password Baru \t: ")
                
                # If newPassword != newRePassword
                while newPassword != newRePassword:
                    print("\n==== Password tidak sama! ====")
                    newPassword = input("Password Baru \t\t: ")
                    newRePassword = input("Ulangi Password Baru \t: ")
                
                # Change Password Success
                user['password'] = newPassword
                saveUsers(users)
                print("\nPassword berhasil diubah!")
                break
        else:
            print("Password salah!")
            continue
        break
    
# Delete Account (only for visitor)
def deleteAccount(userId):
    users = loadUsers()
    
    # Delete target ID
    data = []
    for user in users:
        if user['user_id'] != userId:
            data.append(user)
    
    saveUsers(data)