from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримую поточну дату
    today = datetime.today().date()
    # Створюю пустий список для майбутніх привітань
    upcoming_birthdays = []
    
    for user in users:
        # Перетворюю дату народження з рядка у datetime-об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Створюю дату народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув у цьому році, переношу на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        # Визначаю різницю між днем народження та сьогоднішньою датою
        delta_days = (birthday_this_year - today).days

        # Додаю перевірку для дебагу
        print(f"Перевіряю {user['name']}: Дата народження {birthday_this_year}, Залишилось днів {delta_days}")

        # Якщо день народження у проміжку 0-7 днів від сьогодні
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на вихідний, переношу на наступний понеділок
            if birthday_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
                shift_days = 7 - birthday_this_year.weekday()
                congratulation_date += timedelta(days=shift_days)
                print(f"Переношу привітання {user['name']} на {congratulation_date}")

            # Додаю користувача у список привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Тестові дані
users = [
    {"name": "John Doe", "birthday": "1985.03.10"},  # Тест на день народження в межах 7 днів
    {"name": "Jane Smith", "birthday": "1990.03.15"}, # Тест на 7-й день від сьогодні
    {"name": "Alice Johnson", "birthday": "1992.03.09"},  # Тест на сьогодні
    {"name": "Bob Brown", "birthday": "1988.03.08"},  # Тест на день у минулому (не має потрапити)
    {"name": "Charlie White", "birthday": "1995.03.16"}  # Тест на поза межами 7 днів (не має потрапити)
]

# Виконую функцію
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
