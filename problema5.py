entrada = input("Digite a nota: ").strip()

try:
    nota = float(entrada)

    if nota < 0 or nota > 10:
        print("Nota inválida.")
    elif nota >= 7:
        print("Aprovado.")
    elif nota >= 5:
        print("Recuperação.")
    else:
        print("Reprovado.")

except ValueError:
    print("Digite uma nota válida.")
