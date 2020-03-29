def sumaPrimos():
    suma = 0
    for i in range(0,30):
        num = int(input("ingrese un numero: "))

        if num != 1:
            for i in range(2, num):

                #si no es primo
                if (num % i) == 0:

                    break
            else:#de lo contrario
                suma = suma + num

    print("La sumatoria total es: "+str(suma))


sumaPrimos()
