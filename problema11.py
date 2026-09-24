n = int(input("Digite N: "))

contador = 0

for numero in range(1, n + 1):
    if numero % 2 == 0:
        contador += 1

print("Quantidade de números pares:", contador)
