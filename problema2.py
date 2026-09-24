soma = float(input("Digite a soma das notas: "))
quantidade = int(input("Digite a quantidade de notas: "))

if quantidade == 0:
    print("Erro: não é possível dividir por zero.")
else:
    media = soma / quantidade
    print("Média:", media)
