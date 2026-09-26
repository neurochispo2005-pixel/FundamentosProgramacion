# Alumno: Aldo Villarreal Pasaran
# Asignatura: Fundamentos de programacion

# Programa para registrar pedidos de McDonald's

# Lista de productos
productos = ["Big Mac", "McChicken", "McNuggets", "Papas", "Refresco"]

# Lista de listas (matriz)
menu = [
    ["Big Mac", 89, 10],
    ["McChicken", 79, 10],
    ["McNuggets", 75, 10],
    ["Papas", 45, 10],
    ["Refresco", 35, 10]
]

# Diccionario con los precios
precios = {
    "Big Mac": 89,
    "McChicken": 79,
    "McNuggets": 75,
    "Papas": 45,
    "Refresco": 35
}

# Tupla con los estados de ánimo
estados = ("Feliz", "Triste", "Emocionado", "Con hambre")


# Función que no regresa valor
def mostrar_menu():
    print("\n--- MENÚ DE McDONALD'S ---")
    for i in range(len(menu)):
        print(i + 1, ".", menu[i][0], "- $", menu[i][1])


# Función que regresa un valor
def calcular_total(pedido):
    total = 0
    for producto in pedido:
        nombre = producto[0]
        cantidad = producto[1]
        total = total + precios[nombre] * cantidad
    return total


# Función para guardar el pedido
def guardar_pedido(pedido, total):
    try:
        archivo = open("pedido.txt", "w")
        archivo.write("PEDIDO DE McDONALD'S\n")
        

        for producto in pedido:
            nombre = producto[0]
            cantidad = producto[1]
            subtotal = precios[nombre] * cantidad

            archivo.write(nombre + " x " + str(cantidad))
            archivo.write(" = $" + str(subtotal) + "\n")

        archivo.write("--------------------\n")
        archivo.write("TOTAL: $" + str(total) + "\n")
        archivo.close()

        print("\nEl pedido se guardó correctamente.")
    except:
        print("Error al guardar el archivo.")


# Función para leer el pedido
def leer_pedido():
    try:
        archivo = open("pedido.txt", "r")
        print("\n--- PEDIDO GUARDADO ---")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except:
        print("Error al leer el archivo.")


# Programa principal

pedido = []

print("================================")
print("    SISTEMA DE McDONALD'S")
print("================================")

nombre_cliente = input("Ingresa el nombre del cliente: ")

# while para registrar varios productos
continuar = "si"

while continuar == "si":
    mostrar_menu()
    
    # Leemos la entrada como texto para validar si es puramente un número entero
    entrada_opcion = input("\nSelecciona un producto (1-5): ")

    # .isdigit() verifica que todos los caracteres sean dígitos (evita decimales como "3.4" y letras)
    if entrada_opcion.isdigit():
        opcion = int(entrada_opcion)

        if opcion >= 1 and opcion <= 5:
            producto = menu[opcion - 1][0]

            entrada_cantidad = input("Ingresa la cantidad: ")
            
            if entrada_cantidad.isdigit():
                cantidad = int(entrada_cantidad)

                if cantidad > 0:
                    pedido.append([producto, cantidad])
                    print("Producto agregado:", producto)
                    
                    # PREGUNTA MOVIDA: Solo se pregunta si el flujo fue completamente exitoso
                    continuar = input("\n¿Quieres agregar otro producto? (si/no): ").lower()
                    while continuar != "si" and continuar != "no":
                        continuar = input("¿Quieres agregar otro producto? (si/no): ").lower()
                else:
                    print("La cantidad debe ser mayor a cero.")
            else:
                print("Error: la cantidad debe ser un número entero.")
        else:
            print("Opción no válida.")
    else:
        print("Error: debes ingresar un número entero válido (sin puntos ni letras).")


# Calcular total
total = calcular_total(pedido)

print("\n================================")
print("        RESUMEN")
print("================================")

print("Cliente:", nombre_cliente)

for producto in pedido:
    nombre = producto[0]
    cantidad = producto[1]
    print(nombre, "x", cantidad, "= $", precios[nombre] * cantidad)

print("TOTAL A PAGAR: $", total)


# Retroalimentación
print("\n--- RETROALIMENTACIÓN ---")
print("¿Cómo te sientes?")
for i in range(len(estados)):
    print(i + 1, ".", estados[i])

try:
    opcion_estado = int(input("Selecciona una opción: "))
    if opcion_estado >= 1 and opcion_estado <= 4:
        estado = estados[opcion_estado - 1]
    else:
        estado = "No especificado"
except ValueError:
    estado = "No especificado"

comentario = input("Escribe una opinión sobre nuestro servicio: ")

print("\nGracias por tu opinión,", nombre_cliente)
print("Estado de ánimo:", estado)
print("Comentario:", comentario)

# Guardar información en un archivo
guardar_pedido(pedido, total)

# Leer nuevamente el archivo
leer_pedido()

# GRACIAS