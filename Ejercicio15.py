def binario(num):
    numBinario = ""

    while True:
        if num // 2 <= 0:
            break
        else:
            numBinario = str(num % 2) + numBinario
            num = num // 2

    print(str(num)+numBinario)


num = int(input("Ingrese un numero Entero: "))
binario(num)