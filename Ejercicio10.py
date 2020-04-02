print("leer 3 numeros y mostrar el mayor de ellos")
lista = []#iniciamos una lista vacia

i=0

for i in range(0,3):
    num = int(input("Ingrese el numero: "+str(i+1)+": "))

    lista.append(num)

def numMayor(lista):
    # ciclo burbuja para reordenamiento de valores
    for i in range(0, 3):
        j = i
        for j in range(0, 3):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j = j + 1
        i = i + 1

    print("El numero mayor es: ", lista[0])

numMayor(lista)



