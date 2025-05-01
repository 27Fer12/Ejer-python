datos_temperatura ={
    "mañana": 20,
    "tarde": 25,
    "noche": 18
    }



def predecir_temperatura(hora):
    if hora =="mañana":
        return datos_temperatura["mañana"]
    elif hora == "tarde":
        return datos_temperatura["tarde"]
    elif hora =="tarde":
        return datos_temperatura["noche"]
    elif hora == "noche"