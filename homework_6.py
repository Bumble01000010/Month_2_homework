SECRET_PASSWORD = "kitty_2007"

def password_guard(func):
    def wrapper(*args, **kwargs):
        if SECRET_PASSWORD == args[0]:
            return func(*args, **kwargs)
        else:
            return "🚨 СИГНАЛИЗАЦИЯ! Доступ запрещён"
    return wrapper

@password_guard
def open_vault(password, money):
    print("Сейф открыт!")
    return f"Забирайте {money} сом"

print(open_vault("kitty_2007", 100))
print(open_vault("123", 100))