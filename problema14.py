entrada = input("Digite o preço do produto: ").strip()

if entrada == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(entrada)

        if preco < 0:
            print("O preço não pode ser negativo.")
        else:
            print("Preço:", preco)

    except ValueError:
        print("Digite um preço válido.")
