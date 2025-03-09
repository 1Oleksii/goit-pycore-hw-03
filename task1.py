from datetime import datetime  # Імпортую модуль datetime для роботи з датами

def get_days_from_today(date: str) -> int:
    """
    Обчислюю кількість днів між заданою датою та сьогоднішнім днем.
    
    :param date: Рядок у форматі 'РРРР-ММ-ДД'
    :return: Ціле число, що представляє різницю в днях
    """
    try:
        # Перетворюю рядок дати у об'єкт datetime
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримую поточну дату без урахування часу
        today_date = datetime.today().date()
        
        # Розраховую різницю між поточною датою і заданою
        delta = today_date - given_date
        
        # Повертаю кількість днів як ціле число
        return delta.days
    except ValueError:
        # Обробляю виняток, якщо формат дати неправильний
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

# Приклад виклику функції
print(get_days_from_today("2021-10-09"))  # Виводжу кількість днів від 9 жовтня 2021 до сьогодні
