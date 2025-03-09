import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряю, чи параметри знаходяться в правильних межах
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Використовую множину для забезпечення унікальності чисел
    unique_numbers = set()
    
    # Генерую унікальні випадкові числа
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min, max))
    
    # Повертаю відсортований список чисел
    return sorted(list(unique_numbers))

# Приклад використання функції:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
