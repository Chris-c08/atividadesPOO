def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota: "))

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")


def cadastrar_aluno():
    nome = input("Digite o nome: ").strip()

    if nome == "":
        print("Erro: o nome não pode ficar vazio.")
        return

    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade > 0:
                break

            print("A idade deve ser maior que zero.")

        except ValueError:
            print("Digite uma idade válida.")

    nota1 = ler_nota(1)
    nota2 = ler_nota(2)
    nota3 = ler_nota(3)

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print("\n--- RESULTADO ---")
    print("Nome:", nome)
    print("Idade:", idade)
    print(f"Média: {media:.2f}")
    print("Situação:", situacao)


cadastrar_aluno()
