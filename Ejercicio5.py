print("IIngrese un numero y muestre su tabla de multiplicar")


def tabla():
    n1 = int(input("Ingrese un numero entero para mostrar su tabla de multiplicar: "))
    for i in range(1,11):
        print(n1,"*",i,"= ",n1*i)

tabla()