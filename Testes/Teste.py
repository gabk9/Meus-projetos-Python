id = 0
nome = ""
sal = 0.0
br = True # Variável do tipo bool

id = int(input("Me diga sua idade: ")) 
nome = str(input("Me diga seu nome: ")) 
sal = float(input("Me diga seu salario: ")) # Por padrão ele só irá mostrar uma casa depois da virgula 

resposta = input("Você é brasileiro? (s/n) ").strip().lower() # strip remove espaços em branco, e lower coloca todas as letras em minúsculo 

if resposta == 's':
    br = True  
else:
    br = False

print(f"\n\nSua idade é: {id}")
print(f"Seu nome é: {nome}")
print(f"O seu salário é: {sal}")
print(f"\"Você é brasileiro?\", BR = {br}")