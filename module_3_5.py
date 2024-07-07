# Рекурсия
# Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    if number < 10:
        return number
    else:
        return get_multiplied_digits(number//10) * max(1,(number % 10))

print(get_multiplied_digits(40203))
print(get_multiplied_digits(100))


