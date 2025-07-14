PESSOAS = {"gabriel": 15, "lucas": 15, "david": 15, "esdras": 16}
nome = str(input("Diga-me um nome para buscar: ")).lower()
idade = PESSOAS.get(nome)
if idade:
    print(f"{nome} tem {idade} anos!")
else:
    print("Não encontrado!")