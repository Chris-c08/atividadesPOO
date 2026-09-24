entrada = input("Digite o preço: ").strip()

try:
    preco = float(entrada)

    if preco < 0:
        print("O preço não pode ser negativo.")
    else:
        quantidade = int(input("Digite a quantidade: "))
        total = preco * quantidade
        print("Valor total:", total)

except ValueError:
    print("Digite um preço numérico válido.")
