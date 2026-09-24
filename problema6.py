senha_correta = "Python123"
max_tentativas = 3

for tentativa in range(1, max_tentativas + 1):
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta.")

else:
    print("Número máximo de tentativas atingido.")
