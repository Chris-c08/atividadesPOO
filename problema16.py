try:
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError:
    print("Erro: o arquivo alunos.txt não foi encontrado.")
