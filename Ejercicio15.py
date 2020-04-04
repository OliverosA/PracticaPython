def finobacci():
    b = 0
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

