def resultado():
    suma = 0

    for i in range(2, 50, 3):
        if i % 5 == 0:
            suma = suma + i

    print("La suma es: ", suma)


resultado()