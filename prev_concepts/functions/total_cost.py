def value_plan(minutes):
    value_base_plan = 15000
    new_value_plan = 15000

    for _ in range(minutes):
        new_value_plan += 200

    if new_value_plan > value_base_plan:
        return new_value_plan
    else:
        return value_base_plan


minutes = int(input("minutos extra: "))


print(value_plan(minutes))
