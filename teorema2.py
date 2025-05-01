# Ejemplo simple de adquisición de conocimiento a través de la observación

# El sistema aprenderá la relación entre las horas del día y la temperatura promedio
datos_temperatura = {
    "mañana": 20,
    "tarde": 25,
    "noche": 18,
    "medianoche": 15,
    "mediodía": 28
}

ciudades = {
    20: "Ciudad de México",
    25: "oaxaca",
    18: "tlaxiaco",
    15: "putla",
    28: "puebla"
}

def encontrar_ciudad_por_temperatura(temperatura):
    return ciudades.get(temperatura, "No hay una ciudad registrada con esa temperatura")

temperatura = int(input("Ingrese la temperatura en °C: "))
ciudad = encontrar_ciudad_por_temperatura(temperatura)
print(f"La ciudad con {temperatura}°C es: {ciudad}.")
