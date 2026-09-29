# ALUMNO: Aldo Villarreal Pasaran
# ASIGNATURA: Fundamentos de programacion
# SISTEMA DE PEDIDOS DE McDONALD'S

import time
import os
import pdb

productos = [                                                # Datos
    "Big Mac", "McChicken", "McNuggets", "Papas", "Refresco"  
]

menu = [                                   # Matriz: producto, precio y existencia
    ["Big Mac", 89, 150],
    ["McChicken", 79, 120],
    ["McNuggets", 75, 180],
    ["Papas", 45, 250],
    ["Refresco", 35, 300]
]

precios = {                                # Diccionario de precios
    "Big Mac": 89,
    "McChicken": 79,
    "McNuggets": 75,
    "Papas": 45,
    "Refresco": 35
}

estados = ("Feliz", "Triste", "Emocionado", "Con hambre")      # Tupla de estados

def pantalla_carga():                     # Funciones del programa
    print("\nIniciando sistema...")
    for i in range(1, 6):
        print("Cargando", i * 20, "%")
        time.sleep(0.5)
    print("Sistema listo.\n")

def capturar_fecha():
    while True:
        try:
            dia = int(input("Ingresa el dia: "))
            mes = int(input("Ingresa el mes: "))
            anio = int(input("Ingresa el anio: "))

            if not 1 <= dia <= 31:
                print("Dia no valido.")
                continue

            if not 1 <= mes <= 12:
                print("Mes no valido.")
                continue

            if anio < 2000:
                print("Anio no valido.")
                continue

            Fecha = dia, mes, anio
            return Fecha

        except ValueError:
            print("Error: utiliza numeros enteros.")

def fecha_texto(Fecha):
    dia, mes, anio = Fecha
    return str(dia).zfill(2) + "/" + str(mes).zfill(2) + "/" + str(anio)

def bienvenida(nombre):
    mensaje = "Bienvenido/a " + nombre + " al sistema de McDonald's."
    print("\n================================")
    print(mensaje)
    print("Fecha:", fecha_texto(Fecha))
    print("================================")

def mostrar_menu():
    print("\n------------- MENU -------------")
    for i in range(len(menu)):
        print(
            i + 1, ".",
            menu[i][0],
            "- $", menu[i][1],
            "- Disponibles:", menu[i][2]
        )
    print("--------------------------------")

def registrar_pedido():
    pedido = []
    continuar = "si"

    while continuar == "si":
        mostrar_menu()

        opcion_texto = input("\nSelecciona un producto (1-5): ")

        if not opcion_texto.isdigit():
            print("Error: debes ingresar un numero entero.")
            continue

        opcion = int(opcion_texto)

        if opcion < 1 or opcion > 5:
            print("Opcion no valida.")
            continue

        producto = menu[opcion - 1][0]
        existencia = menu[opcion - 1][2]

        cantidad_texto = input("Ingresa la cantidad: ")

        if not cantidad_texto.isdigit():
            print("Error: cantidad no valida.")
            continue

        cantidad = int(cantidad_texto)

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            continue

        if cantidad > existencia:         # CORRECCION: no permite cantidades mayores a la de existencia
            print("ERROR: no hay suficiente existencia.")
            print("Disponibles:", existencia)
            print("Solicitados:", cantidad)
            continue

        pedido.append([producto, cantidad])
        menu[opcion - 1][2] -= cantidad

        print("Producto agregado:", producto)
        print("Existencia restante:", menu[opcion - 1][2])

        continuar = input(
            "\n¿Quieres agregar otro producto? (si/no): "
        ).lower()

        while continuar != "si" and continuar != "no":
            continuar = input(
                'Escribe solamente "si" o "no": '
            ).lower()

    return pedido

def calcular_total(pedido):
    total = 0

    for producto in pedido:
        nombre = producto[0]
        cantidad = producto[1]
        total += precios[nombre] * cantidad

    return total

def mostrar_resumen(pedido, total, cliente):
    print("\n================================")
    print("             RESUMEN")
    print("================================")
    print("Cliente:", cliente)
    print("Fecha:", fecha_texto(Fecha))

    for producto in pedido:
        nombre = producto[0]
        cantidad = producto[1]
        subtotal = precios[nombre] * cantidad
        print(nombre, "x", cantidad, "= $", subtotal)

    print("--------------------------------")
    print("EL TOTAL ES: $", total)

def obtener_estado():
    print("\n--- RETROALIMENTACION ---")

    for i in range(len(estados)):
        print(i + 1, ".", estados[i])

    try:
        opcion = int(input("Selecciona una opcion: "))

        if 1 <= opcion <= 4:
            return estados[opcion - 1]

        print("Opcion no valida.")
        return "No especificado"

    except ValueError:
        print("Debes ingresar un numero entero.")
        return "No especificado"

def guardar_pedido(pedido, total, cliente):     # Archivos
    try:
        archivo = open("pedido.txt", "a", encoding="utf-8") # "a" conserva los pedidos anteriores.
        archivo.write("\n==============================\n")
        archivo.write("       NUEVO PEDIDO\n")
        archivo.write("==============================\n")
        archivo.write("Cliente: " + cliente + "\n")
        archivo.write("Fecha: " + fecha_texto(Fecha) + "\n")

        for producto in pedido:
            nombre = producto[0]
            cantidad = producto[1]
            subtotal = precios[nombre] * cantidad

            archivo.write(
                nombre + " x " + str(cantidad)
                + " = $" + str(subtotal) + "\n"
            )

        archivo.write("------------------------------\n")
        archivo.write("TOTAL: $" + str(total) + "\n")
        archivo.close()

        print("Pedido guardado en el historial.")

    except PermissionError:
        print("Error: no tienes permisos para escribir.")

    except OSError:
        print("Error al guardar pedido.txt.")

def guardar_cliente(cliente):
    try:
        archivo = open("cliente.txt", "w", encoding="utf-8")
        archivo.write("INFORMACION DEL CLIENTE\n")
        archivo.write("Nombre: " + cliente + "\n")
        archivo.write("Fecha: " + fecha_texto(Fecha) + "\n")
        archivo.close()

    except PermissionError:
        print("Error de permisos en cliente.txt.")

    except OSError:
        print("Error al guardar cliente.txt.")

def guardar_opinion(cliente, estado, comentario):
    try:
        archivo = open("opinion.txt", "w", encoding="utf-8")
        archivo.write("RETROALIMENTACION\n")
        archivo.write("Cliente: " + cliente + "\n")
        archivo.write("Fecha: " + fecha_texto(Fecha) + "\n")
        archivo.write("Estado: " + estado + "\n")
        archivo.write("Comentario: " + comentario + "\n")
        archivo.close()

    except PermissionError:
        print("Error de permisos en opinion.txt.")

    except OSError:
        print("Error al guardar opinion.txt.")

def guardar_reporte(pedido, total, cliente):
    try:
        archivo = open("reporte.txt", "w", encoding="utf-8")
        archivo.write("REPORTE DEL PEDIDO\n")
        archivo.write("Cliente: " + cliente + "\n")
        archivo.write("Fecha: " + fecha_texto(Fecha) + "\n")

        for producto in pedido:
            archivo.write(
                producto[0] + " x "
                + str(producto[1]) + "\n"
            )

        archivo.write("TOTAL: $" + str(total) + "\n")
        archivo.close()

    except PermissionError:
        print("Error de permisos en reporte.txt.")

    except OSError:
        print("Error al guardar reporte.txt.")

def mostrar_archivos():
    archivos = [
        "pedido.txt",
        "cliente.txt",
        "opinion.txt",
        "reporte.txt"
    ]

    print("\n--- ARCHIVOS DISPONIBLES ---")

    for i in range(len(archivos)):
        if os.path.exists(archivos[i]):
            print(i + 1, ".", archivos[i])
        else:
            print(i + 1, ".", archivos[i], "(no creado)")

    return archivos

def leer_archivo(nombre):
    try:
        archivo = open(nombre, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()

        print("\n---", nombre, "---")
        print(contenido)

    except FileNotFoundError:
        print("Error: el archivo no existe.")

    except PermissionError:
        print("Error: no tienes permisos para leerlo.")

    except OSError:
        print("Error al leer el archivo.")

def consultar_archivos():
    archivos = mostrar_archivos()

    while True:
        try:
            opcion = int(input("Selecciona un archivo (1-4): "))

            if 1 <= opcion <= 4:
                leer_archivo(archivos[opcion - 1])
                break

            print("Selecciona una opcion entre 1 y 4.")

        except ValueError:
            print("Debes ingresar un numero entero.")

def anexar_observacion():
    try:
        texto = input("Escribe una observacion: ")

        archivo = open("pedido.txt", "a", encoding="utf-8")
        archivo.write("\nOBSERVACION: " + texto + "\n")
        archivo.write("Fecha: " + fecha_texto(Fecha) + "\n")
        archivo.close()

        print("Observacion agregada.")

    except FileNotFoundError:
        print("Primero debes crear un pedido.")

    except PermissionError:
        print("No tienes permisos para modificar el archivo.")

    except OSError:
        print("Error al modificar pedido.txt.")

def control_inactividad():                            # Función de inactividad
    print("\nControl de inactividad: 10 minutos.")

    for segundo in range(600):                         # 600 segundos = 10 minutos.

        if segundo > 0 and segundo % 60 == 0:
            print(
                "Tiempo transcurrido:",
                segundo // 60,
                "minuto(s)"
            )

        time.sleep(1)

    print("\nSe alcanzaron los 10 minutos.")

    while True:
        respuesta = input(
            '¿Quieres continuar? (si/no): '
        ).lower()

        if respuesta == "si":
            return True

        if respuesta == "no":
            return False

        print('Escribe solamente "si" o "no".')


# -------------------- PROGRAMA PRINCIPAL --------------------

print("================================")
print("    SISTEMA DE McDONALD'S")
print("================================")

pantalla_carga()

while True:
    nombre_cliente = input(
        "Ingresa el nombre del cliente: "
    ).strip()

    if nombre_cliente != "":
        break

    print("El nombre no puede estar vacio.")


Fecha = capturar_fecha()

bienvenida(nombre_cliente)

pedido = registrar_pedido()

total = calcular_total(pedido)

mostrar_resumen(
    pedido,
    total,
    nombre_cliente
)

estado = obtener_estado()

comentario = input(
    "Escribe una opinion sobre el servicio: "
)

print("\nGracias por tu opinion,", nombre_cliente)
print("Estado de animo:", estado)
print("Comentario:", comentario)

guardar_pedido(
    pedido,
    total,
    nombre_cliente
)

guardar_cliente(nombre_cliente)

guardar_opinion(
    nombre_cliente,
    estado,
    comentario
)

guardar_reporte(
    pedido,
    total,
    nombre_cliente
)

mostrar_archivos()

consultar = input(
    "\n¿Quieres consultar un archivo? (si/no): "
).lower()

if consultar == "si":
    consultar_archivos()

anexar = input(
    "\n¿Quieres agregar una observacion? (si/no): "
).lower()

if anexar == "si":
    anexar_observacion()

print("\n================================")
print("       PROGRAMA FINALIZADO")
print("================================")
print("Gracias,", nombre_cliente)
print("Fecha:", fecha_texto(Fecha))