def resultado():

    suma =0
    numero = (int(input("ingrese un numero: ")))
    if numero >= 0:
        suma = suma + numero
        while numero >= 0:
            numero = (int(input("ingrese un numero ")))
            if numero >= 0:
                suma = suma + numero

        print("la suma es :", suma)
    else:
        print("Debe Ingresar Un Numero mayor o Igual a 0")



resultado()