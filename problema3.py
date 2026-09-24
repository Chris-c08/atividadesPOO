nomes = ["Ana", "Bruno", "Carlos", "Daniel"]

indice = int(input("Digite o índice: "))

if 0 <= indice < len(nomes):
    print("Aluno:", nomes[indice])
else:
    print("Índice inválido.")
