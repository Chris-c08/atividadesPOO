identificador = input("Digite o identificador: ").strip()

if len(identificador) == 11 and identificador.isdigit():
    print("Identificador válido.")
else:
    print("Identificador inválido.")
