# Bienvenida
total = 0

# Variable para saber si el cliente quiere continuar
continuar = "S"

print("BIENVENIDO A MCDONALD'S")

# Repite el programa mientras el cliente quiera comprar
while continuar == "S" or continuar == "s":

    # Mostramos el menú de productos
    print("NUESTRO MENU ES:")
    print("1. Big Mac - $170")
    print("2. McChicken - $65")
    print("3. McNuggets - $120")
    print("4. Papas - $45")
    print("5. Refresco - $35")

     # Pedimos al cliente que seleccione un producto
    opcion = int(input("Selecciona un producto: "))  

    # Preguntamos si quiere algo más
    continuar = input("¿Quieres algo mas? (S/N): ")

# Mostramos el resultado
print("Gracias por tu compra.")
