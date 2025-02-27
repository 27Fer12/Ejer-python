import math
import random
import datetime

def ejercicio1():
    nombre = "Juan"
    edad = 25
    altura = 1.75
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Altura:", altura)

def ejercicio2():
    nombre = "Juan"
    edad = 25
    altura = 1.75
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Altura:", altura)

def ejercicio3():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    altura = float(input("¿Cuánto mides? (en metros) "))
    print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

def ejercicio4():
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    numero3 = float(input("Introduce el tercer número: "))
    numero4 = float(input("Introduce el cuarto número: "))
    resta = numero1 - numero2
    multiplicacion = numero3 * numero4
    print(f"El resultado de la resta de {numero1} - {numero2} es: {resta}")
    print(f"El resultado de la multiplicación de {numero3} * {numero4} es: {multiplicacion}")

def ejercicio5():
    radio = float(input("Introduce el radio del círculo en metros: "))
    area = math.pi * (radio ** 2)
    print(f"\nEl área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

def ejercicio6():
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        print(f"{num} es par.")
    else:
        print(f"{num} es impar.")

def ejercicio7():
    num = int(input("Ingresa un número: "))
    if num > 10:
        print(f"{num} es mayor que 10.")
    else:
        print(f"{num} no es mayor que 10.")

def ejercicio8():
    num = int(input("Ingresa un número: "))
    if num > 0:
        print(f"{num} es positivo.")
    elif num < 0:
        print(f"{num} es negativo.")
    else:
        print("El número es cero.")

def ejercicio9():
    numero_aleatorio = random.randint(1, 10)
    adivina = int(input("Adivina el número entre 1 y 10: "))
    print(f"El número aleatorio es {numero_aleatorio}.")
    if adivina == numero_aleatorio:
        print("¡Correcto! Has adivinado el número.")
    else:
        print(f"Incorrecto. El número era {numero_aleatorio}.")

def ejercicio10():
    nota = int(input("Ingresa tu calificación (0-100): "))
    if 90 <= nota <= 100:
        print("Tu calificación es: 'A'")
    elif 80 <= nota < 90:
        print("Tu calificación es: 'B'")
    elif 70 <= nota < 80:
        print("Tu calificación es: 'C'")
    elif 60 <= nota < 70:
        print("Tu calificación es: 'D'")
    else:
        print("Tu calificación es: 'F'")

def ejercicio11():
    nombre = input("Ingresa tu nombre: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Nombre del cliente: {nombre} y la fecha y hora: {fecha}")

def ejercicio12():
    nombre = input("Ingresa tu nombre: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Nombre del cliente: {nombre} y la fecha y hora: {fecha}")

def ejercicio13():
    total_compra = float(input("Ingresa el total de tu compra: "))
    if total_compra > 100:
        descuento = total_compra * 0.10
        total_final = total_compra - descuento
        print(f"¡Felicidades! Tienes un descuento del 10%. El total a pagar es: {total_final:.2f}")
    else:
        print(f"El total a pagar es: {total_compra:.2f}")

def ejercicio14():
    nombre_tienda = input("Ingresa el nombre de la tienda: ").strip()
    nombre = input("Ingresa tu nombre: ").strip()
    producto = input("Ingresa el nombre del producto: ").strip()
    while True:
        try:
            total_compra = float(input("Ingresa el total de tu compra: "))
            if total_compra < 0:
                print("El total de la compra no puede ser negativo. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
    folio = random.randint(10000, 99999)
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    descuento = total_compra * 0.10 if total_compra > 100 else 0
    total_final = total_compra - descuento
    print("\n=====================================")
    print("         TICKET DE COMPRA           ")
    print("=====================================")
    print(f"Tienda: {nombre_tienda}")
    print(f"Folio: {folio}")
    print(f"Fecha y hora: {fecha_hora}")
    print("\nCliente:  ", nombre)
    print("Producto: ", producto)
    print(f"Total de la compra:  ${total_compra:.2f}")
    print(f"Descuento aplicado:   ${descuento:.2f}")
    print(f"Total a pagar:        ${total_final:.2f}")
    print("\n=====================================")
    print("¡Gracias por tu compra! ¡Vuelve pronto!")
    print("=====================================")

def tomar_decision(prioridades):
    opciones = ["ir al cine", "estudiar", "hacer ejercicio"]
    for opcion in prioridades:
        if opcion in opciones:
            return f"El agente decide: {opcion}"
    return "El agente no decide nada."

def ejercicio15():
    prioridades = ["hacer ejercicio", "estudiar"]
    print(tomar_decision(prioridades))

class Agente:
    def __init__(self, nombre, ubicacion): 
        self.nombre = nombre
        self.ubicacion = ubicacion

    def mover(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"{self.nombre} se movió a {self.ubicacion}")

def ejercicio16():
    agente1 = Agente("Agente 1", "A")
    agente2 = Agente("Agente 2", "B")

    agente1.mover("C")
    agente2.mover("C")

    if agente1.ubicacion == agente2.ubicacion:
        print("Los agentes se han encontrado en el punto C.")
    else:
        print("Los agentes no se han encontrado.")

def heuristica(a, b):
    return abs(a - b)

def ejercicio17():
    objetivo = 50
    valores = [20, 35, 55, 60, 70]
    mejor_valor = min(valores, key=lambda x: heuristica(x, objetivo))
    print(f"El valor más cercano al objetivo {objetivo} es: {mejor_valor}")

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return visitados

def ejercicio18():
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C'],
    }
    resultado = dfs(grafo, 'A')
    print(f"Nodos visitados por DFS: {resultado}")

import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica(inicio), 0, inicio, []))  # (f, g, nodo, camino)
    visitados = {}
    
    while cola_prioridad:
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        
        if nodo in visitados and visitados[nodo] <= g:
            continue
        
        visitados[nodo] = g
        camino = camino + [nodo]
        
        if nodo == objetivo:
            return camino
        
        for vecino, costo in grafo.get(nodo, []):
            heapq.heappush(cola_prioridad, (g + costo + heuristica(vecino), g + costo, vecino, camino))
    
    return None  

def ejercicio19():
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
    }

    def heuristica(nodo):
        distancias = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
        return distancias.get(nodo, float('inf'))

    camino = a_estrella(grafo, 'A', 'D', heuristica)
    print(f"El camino más corto es: {camino}")

def ejercicio20():
    def funcion_objetivo(x):
        return x**2 - 4*x + 4  

    def descenso_colina(inicio, tasa_aprendizaje=0.1, iteraciones=100):
        x = inicio
        for _ in range(iteraciones):
            gradiente = 2*x - 4  
            x = x - tasa_aprendizaje * gradiente  
        return x

    solucion = descenso_colina(0)
    print(f"La solución óptima es: {solucion}")

def mostrar_menu():
    menu = {
        1: ("Declaración de variables", ejercicio1),
        2: ("Declaración y suma de variables", ejercicio2),
        3: ("Entrada de datos", ejercicio3),
        4: ("Resta y multiplicación", ejercicio4),
        5: ("Cálculo del área de un círculo", ejercicio5),
        6: ("Verificar si un número es par", ejercicio6),
        7: ("Verificar si un número es mayor que 10", ejercicio7),
        8: ("Clasificación de números", ejercicio8),
        9: ("Juego de adivinanza", ejercicio9),
        10: ("Clasificación de notas", ejercicio10),
        11: ("Uso de librería datetime", ejercicio11),
        12: ("Declaración y suma de variables", ejercicio12),
        13: ("Ejercicio 13", ejercicio13),
        14: ("Menú ejercicio", ejercicio14),
        15: ("Ejercicio 15", ejercicio15),
        16: ("Ejercicio 16", ejercicio16),
        17: ("Ejercicio 17", ejercicio17),
        18: ("Ejercicio 18", ejercicio18),
        19: ("Ejercicio 19", ejercicio19),
        20: ("Ejercicio 20", ejercicio20),
    }
    while True:
        print("\nMenú de Ejercicios")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")
        print("0. Salir")
        opcion = int(input("\nSelecciona una opción: "))
        if opcion == 0:
            break
        elif opcion in menu:
            menu[opcion][1]()
        else:
            print("Opción no válida, intenta de nuevo.")

mostrar_menu()

