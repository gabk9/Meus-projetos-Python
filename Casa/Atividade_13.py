lista = [int(x) for x in input("Me diga uma lista de números separadas por espaço : ").split()]
somaPares = sum(x for x in lista if x % 2 == 0)
print(f"A soma dos números pares da lista é {somaPares}") 