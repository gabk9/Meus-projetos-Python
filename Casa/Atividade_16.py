id = {"fruta1": 0.0,
      "fruta2": 0.0, 
      "fruta3": 0.0, 
      "fruta4": 0.0,
      "fruta5": 0.0} 

qtd = int(input("Quantas frutas deseja adicionar?? (até 5) "))

for i, chave in enumerate(id):
    if i >= qtd:
        break
    nome = input(f"Me diga o nome para a {chave}: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    id[chave] = (nome, preco)

print("\nFrutas adicionadas:")
for chave, valor in id.items():
    if valor != 0.0:
        print(f"{chave}: Nome = {valor[0]}, Preço: R$ {valor[1]:.2f}")