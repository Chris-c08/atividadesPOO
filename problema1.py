entrada = input("Digite sua idade: ").strip()

try:
    if entrada == "":
        raise ValueError

    idade = int(entrada)

    if idade < 0:
        print("Idade inválida.")
    elif idade == 0:
        print("Idade igual a zero.")
    else:
        print(f"Idade válida: {idade}")

except ValueError:
    print("Digite uma idade válida.")
