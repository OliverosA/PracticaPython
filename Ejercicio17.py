print("calcular la media de una secuencia de numeros")
print("el programa terminara cuando el usuario oprima F")


def Media():
    valor = input("Ingrese un valor numerico: ")
    if valor == "f":
        print("F detectada fin del programa")

    elif valor != "f":
        suma = 0
        suma = suma + int(valor)
        contador = 1
        media = suma / contador
        while True:
            print("La media es: ",media)
            valor = input("Ingrese un valor numero o F para terminar: ")
            if valor == "f" or valor == "F":
                break
            else:
                suma = suma + int(valor)
                contador = contador+1
                media = suma / contador


Media()
