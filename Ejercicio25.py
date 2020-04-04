def Factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact


def Formula():
    n = int(input("Ingrese un numero mayor a 0: "))
    while True:
        i = int(input("Ingrese un numero mayor al anterior: "))
        if n<i:
            break
    _formula = Factorial(n)/((Factorial(i))*(Factorial(n-i)))
    print("Resultado: ", _formula)


Formula()
