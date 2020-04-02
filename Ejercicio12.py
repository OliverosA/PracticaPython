import os

print("secuencia de 30 numeros y mostrar la suma y el producto de ellos")

def sumaProducto():
    suma = 0
    producto = 1
    for i in range(0,30):

        n1 = int(input("Ingrese el numero "+str(i+1)+": "))
        suma = suma + n1
        producto = producto * n1


    print("La Suma De La Secuencia Es: ",suma,"\n ","El producto De La Secuencia Es: ",producto)

sumaProducto()