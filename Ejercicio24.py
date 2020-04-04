print("Numero de euler")


def Factorial(x):
    temp = 1
    for i in range(1, x):
        temp = temp * i
    return temp


def Euler():
    e = 0
    limite = int(input("Ingrese el limite: "))
    for i in range(1, limite):
        e = e + 1/Factorial(i)
    print("El numero de Euler es: ", e)


Euler()
