total = 0
visitantes = int(input("¿Cuántos visitantes van a entrar al museo? "))

for i in range(visitantes):

    print("Visitante", i + 1)

    edad = int(input("Ingresa la edad del visitante: "))

    if edad < 0:
        print("Esa edad no es valida. Terminar el programa.")
        break

    if edad < 3:
        print("El visitante es menor de 3 años y no paga boleto.")
        continue

    if edad < 18:
        precio = 30
    else:
        precio = 45

    print("Tipos de visitante:")
    print("1. Adulto mayor")
    print("2. Profesor")
    print("3. Estudiante")

    tipo = int(input("Selecciona el tipo de visitante: "))

    if tipo == 1:
        descuento = precio * 0.12
        precio_final = precio - descuento

    elif tipo == 2:
        descuento = precio * 0.10
        precio_final = precio - descuento

    elif tipo == 3:
        descuento = precio * 0.10
        precio_final = precio - descuento

    else:
        precio_final = precio
    print("Precio a pagar: $", round(precio_final, 2))

    total = total + precio_final
print("El total a pagar por todos los visitantes es: $", round(total, 2))

print("Tabla de datos")
print("Persona\tPrecio\Descuento")
print(f"Visitante1\t{precio_final}\t{descuento}")
print(f"Visitante2\t{precio_final}\t{descuento}")
print(f"Visitante3\t{precio_final}\t{descuento}")
print(f"Visitante4\t{precio_final}\t{descuento}")