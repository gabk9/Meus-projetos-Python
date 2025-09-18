class animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fala(self):
        return f"{self.nome} é um(a) {self.especie}"

class cachorro(animal): 
    def __init__(self, nome, raca):
        super().__init__(nome, "cachorro")
        self.raca = raca

    def fala(self):
        return f"{super().fala()} e late"
    
class gato(animal): 
    def __init__(self, nome, cor):
        super().__init__(nome, "gato")
        self.cor = cor

    def fala(self):
        return f"{super().fala()} e mia"
    
dog = cachorro("Rosa", "Pinscher")
cat = gato("Pandora", "Rajado")

print("Atributos do cachorro:")
print(f"Nome: {dog.nome}\nEspecie: {dog.especie}\nRaça: {dog.raca}\n\n{dog.fala()}\n")

print("Atributos do gato:")
print(f"Nome: {cat.nome}\nEspecie: {cat.especie}\nCor: {cat.cor}\n\n{cat.fala()}")