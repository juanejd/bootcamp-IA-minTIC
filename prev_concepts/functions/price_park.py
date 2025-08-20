def total_cost_park(number_persons):
    price_entrance = 30000

    if number_persons < 0:
        raise ValueError(f"No pueden haber {number_persons} personas")
    total_cost = price_entrance * number_persons
    return total_cost


number_persons = int(input("Ingrese la cantidad de personas: "))

result = total_cost_park(number_persons)

print(result)
