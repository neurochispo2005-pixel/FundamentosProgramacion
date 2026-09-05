tabla = [[0] * 10 for i in range(10)]      # Se crea una matriz 10*10 llena de ceros

for i in range(10):
    for j in range(10):
        tabla[i][j] = (i+1)*(j+1)     # Se llena la matriz con los multiplos de cada fila correspondiente

def mostrar_tabla():           # funcion para imprimir tabla
    print()
    print("    ",end="")
    for i in range(10):
        print(f"{i+1:4}",end="")    # Crea el encabezado horizontal
    print()

    for i in range(10):
        print(f"{i+1:4}",end="")    # Crea el encabezado vertical
        for j in range(10):
            print(f"{tabla[i][j]:4}",end="")      # Se imprimen los datos de la tabla asignandole un espacio de 4 elementos a cada numero
        print()
    print()

def buscar_numero(a,b):
    return tabla[a-1][b-1]   # Se busca en la tabla el dato sin usar la funcion * para obtener el resultado

mostrar_tabla();                # Se imprime la tabla

#se piden los numeros
a = int(input("Introduce el primer numero (de 1 a 10): "))
while a<1 or a>10:              # Se valida que los numeros se encuentren dentro del rango
    print("Numero invalido. Ingresa nuevamente")
    a = int(input("Introduce el primer numero (de 1 a 10): "))

b = int(input("Introduce el segundo numero (de 1 a 10): "))
while b<1 or b>10:
    print("Numero invalido. Ingresa nuevamente")
    b = int(input("Introduce el primer numero (de 1 a 10): "))

c = buscar_numero(a,b)        # se busca el numero correspondiente en la tabla

print("Resultado = ", c)     # Se imprime el resultado