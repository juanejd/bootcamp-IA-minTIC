def traveled_distance(time):
    if time < 0:
        raise ValueError("el tiempo ingresado no puede ser negativo")
    VELOCITY = 8
    distance = VELOCITY * time
    return distance


time = int(input("Ingrese el tiempo en horas: "))

distance = traveled_distance(time)

print(f"se recorrieron {distance} kilometros en {time} horas")
