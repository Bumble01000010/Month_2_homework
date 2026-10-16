SECRET_PASSWORD = "kitty_2007"

def password_guard(func):
    pass

def open_vault(password, money):
    print("Сейф открыт!")
    return f"Забирайте {money} сом"

open_vault = password_guard(open_vault)