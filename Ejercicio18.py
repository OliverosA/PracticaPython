print("leer una secuencia de numeros y mostrar cual es el mayor y menor")
print("el proceso finalizara al ingresar un numero impar")


def numMayor(lista,contador):
    # ciclo burbuja para reordenamiento de valores
    print(contador)
    for i in range(0, contador):
        j = i
        for j in range(0, contador):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j = j + 1
        i = i + 1

    print("el numero mayor es: ", lista[0], "el numero menor es: ", lista[contador-1])


def mayorMenor():
    lista = []
    contador = 0
    while True:
        numero = int(input("Ingrese un valor numerico: "))
        if numero % 2 == 0:
             lista.append(numero)
             contador=contador+1
             numMayor(lista,contador)

        else:
            print("El Numero Es Impar Fin Del Programa")
            break


mayorMenor()
