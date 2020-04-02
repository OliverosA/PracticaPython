#pedimos los numeros
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))


def producto(numero1, numero2):             # definimos el metodo producto con los parametros numero1 y numero2
    aux = 0                                 # creamos un aux inicializado en 0
    for i in range(0,numero2):              # inciamos el bucle for de 0 hasta numero 2
        aux = aux+numero1
        print("El resultado "+str(i)+" es: "+str(aux))

    # mostramos el resultado del producto
    print("el producto es: "+str(aux))


producto(numero1, numero2)