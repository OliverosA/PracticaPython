def divisionRestas(n1,n2):
    cociente = 0
    resto = 0

    while True:
        if n1-n2<0:
            break
        else:
            resto = n1-n2
            cociente = cociente+1
            n1=resto
    print("Cociente: ", cociente, "Resto: ", resto )
    #fin del metodo


n1 = int(input("Ingrese el dividendo: "))
n2 = int(input("Ingrese el divisor: "))
while True:
    if n2>n1:
        print("El divisor no puede ser mayor")
        n2 = int(input("Ingrese el divisor: "))
    elif n1>=n2:
        divisionRestas(n1, n2)
        break
    else:
        break
