ano = int(input("Me diga um ano: "))
print(f"{ano} é bissexto" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else f"{ano} não é bissexto")