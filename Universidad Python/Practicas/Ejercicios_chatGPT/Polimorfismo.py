# Crea una clase base llamada Animal con un método hablar(). Luego, crea subclases como Perro, Gato y Vaca, cada una con su propio método hablar() que imprime un sonido característico.

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return 'Guau!'
    
class Gato(Animal):
    def hablar(self):
        return 'Miau!'
    
class Vaca(Animal):
    def hablar(self):
        return 'Muuu!'
    
Perro = Perro()
Gato = Gato()
Vaca = Vaca()

print(Perro.hablar())
print(Gato.hablar())
print(Vaca.hablar())