valor = float(input("Digite o valor da compra: R$ "))

if valor < 0:
    print("Valor inválido.")
elif valor <= 100:
    total = valor
else:
    total = valor * 0.90

print(f"Valor final: R$ {total:.2f}")
