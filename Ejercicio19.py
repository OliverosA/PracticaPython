print("Leer una secuencia de números y mostrar")
print("la suma de los 30 números que ocupan posiciones de lectura par.")


def LecturaPar():

    suma = 0
    posicionLectura = 0
    while True:
        num = int(input("ingrese un numero: "))
        posicionLectura = posicionLectura + 1
        if posicionLectura % 2 == 0:
            suma = suma + num
    print(suma)


LecturaPar()
