print("Determinar el mayor de una secuencia de numeros")


def numMayor():
    while True:
        fin = "n"
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))

        if (numero1 > numero2):
            print("el primer numero: "+str(numero1) + " Es mayor")
        else:
            print("el segundo numero: "+str(numero2) + " Es mayor")

        respuesta = input("Desea Continuar? Si = s, No = n :")

        if (respuesta == fin):
            break

numMayor()