def factorial():
    _factorial = 0
    numero = int(input("Ingrese un numero mayor a 0: "))

    if numero==0:
        print("El factorial de 0 es 1")
    else:
        _factorial = 1
        for i in range(1,numero+1):
            _factorial = _factorial * i

        print("El factorial del numero ingresado es: "+str(_factorial))


factorial()
