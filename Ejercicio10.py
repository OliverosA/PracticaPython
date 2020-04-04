def bucle():
    producto = 1
    respuesta = ""
    fin = "f"

    while True:
        numero = float(input("Ingrese el numero: "))
        producto = producto * numero
        print(producto)
        respuesta = input("Desea Continuar? Si = s, No = f :")

        if (respuesta == fin):
            break

    print("fin del bucle")

bucle()


