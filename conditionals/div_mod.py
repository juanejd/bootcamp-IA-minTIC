# import random


def divisible(number):
    if number % 3 != 0 or number % 5 != 0:
        return "No es divisible por 3 o 5"
    else:
        return "es divisible por 3 y 5"


for i in range(100):
    # number = random.randint(1, 16)
    result = divisible(i)
    print(f"el numero {i} es {result}")
