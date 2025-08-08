import random


def odd_or_even(number):
    if number < 0:
        raise ValueError("el numero no puede ser negativo")
    if number % 2 == 0:
        return "par"
    else:
        return "impar"


for i in range(10):
    number = random.randint(-3, 100)
    result = odd_or_even(number)
    print(f"el numero {number} es {result}")
