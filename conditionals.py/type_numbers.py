import random


def type_number(number):
    if number > 0:
        return "Positivo"
    return "Negativo"


for i in range(10):
    number = random.randint(-100, 100)
    result = type_number(number)
    print(f"el numero {number} es {result}")
