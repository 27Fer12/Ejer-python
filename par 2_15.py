nombre = input("Ingresa tu nombre: ")
produ = input("Ingresa el producto: ")
total_compra = float(input("Ingresa el tota de tu compra: "))
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Felicidades {nombre}! Tienes un descuento del 10%. de tu producto {produ}. \nEl total a pagar es: {total_final}")
else:
    print(f"El total a pagar es: {total_compra}")