def sumaPares():
    suma = 0

    numero = int(input("Ingresa un numero: "))

    while numero%2==0:
        numero = int(input("Ingrese un numero:"))
        if numero%2==0:
            suma = suma + numero
            print(suma)
        else:
            print("Numero Impar Fin De La Suma")
            break

sumaPares()
