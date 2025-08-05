def galons_needed(galons):
    if galons >= 0:
        distance_for_galon = 40
        total_galons = galons * distance_for_galon
        return total_galons
    raise ValueError("la cantidad de galones no puede ser negativa")


galons = int(input("ingrese cantidad de galones: "))

result = galons_needed(galons)
print(f"la distancia recorrida con {galons} galones es de {result} kilometros")
