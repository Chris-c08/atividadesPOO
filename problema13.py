temperaturas = [25, 31, 18, 27, 31, 20]

maior = temperaturas[0]
menor = temperaturas[0]

for temperatura in temperaturas:
    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
