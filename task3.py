import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонні номери до стандартного формату.
    
    Аргументи:
        phone_number (str): Телефонний номер у будь-якому форматі
        
    Повертає:
        str: Нормалізований телефонний номер з міжнародним кодом
    """
    # Видаляю всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Якщо номер починається з '+', значить міжнародний код вже присутній
    if cleaned_number.startswith('+'):
        return cleaned_number
    
    # Якщо номер починається з '380', додаю лише '+'
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    
    # Якщо номер починається з '0', додаю міжнародний код '+38'
    if cleaned_number.startswith('0'):
        return '+38' + cleaned_number
    
    # У будь-яких інших випадках припускаю, що це український номер без '+'
    # і додаю міжнародний код
    return '+38' + cleaned_number


# Приклад використання:
if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

