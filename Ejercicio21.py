print("leer un numero y determinar si es primo o no es primo")


def sumaPrimos():
    a = 0
    n = int(input("Ingrese numero\n"))
    for i in range(1, n + 1):
        if (n % i == 0):
            a = a + 1
    if (a != 2):
        print("No es primo")
    else:
        print("si es primo")