def finobacci():
    n = 0
    a = 0
    b = 0
    c = 0
    aux = 0

    while True:
        n = int(input("Dame Un Numero Entero Positivo: "))
        if n>0:
            break

    a = 1
    for i in range(0,n):
        print(str(a)+"\t")
        aux = a
        a += b
        b = aux



finobacci()

