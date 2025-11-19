# Libraries
import json
import os

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
            return True, f"Login berhasil! Selamat datang, {user['fullname'].title()}", user['fullname'], user['user_level']

    return False, "Email atau password salah!", "", ""
