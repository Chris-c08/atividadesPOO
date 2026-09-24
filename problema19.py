def analisar_usuario(idade, renda, cadastro):
    
    if idade < 18:
        return "Menor de idade."

    elif renda < 2000:
        return "Maior de idade com renda baixa."

    elif cadastro == "sim":
        return "Usuário aprovado."

    else:
        return "Cadastro não aprovado."
