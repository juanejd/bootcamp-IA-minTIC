def check_numbers_order(numbers):
    for i in range(len(numbers) - 1):
        print(i)
        if numbers[i] > numbers[i + 1]:
            return "no estan en orden creciente"
    return "estan en orden creciente"


numbers = [1, 2, 3]

result = check_numbers_order(numbers)

print(result)
