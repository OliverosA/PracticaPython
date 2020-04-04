def Resfactorial():
    contador = 1
    suma = 0

    while contador <= 30:
        num = int(input("Ingrese un valor: "))
        factorial = 1
        for i in range(1,num+1):
            factorial = factorial * i
            #print(factorial)

        suma = suma + factorial
        contador += 1
    print(suma)


Resfactorial()