with open("Atividade_21.txt", "a+") as file:
    file.seek(0)
    linha = file.readline()

print(f"O arquivo tem {len(linha)} linhas")