class Estudiante:

    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
        self.promedio = sum(notas) / len(notas)

    def agregar_nota(self, nota):
        self.notas.append(nota)
        self.promedio = sum(self.notas) / len(self.notas)

    def info(self):
        return f"{self.nombre} tiene {self.edad} años, su promedio es {self.promedio}"

    def esta_aprobado(self):
        if(self.promedio >= 5):
            return True
        else:
            return False

fernando = Estudiante("Fernando",26,[5,4,3,2,6,7,9])

print(Estudiante.esta_aprobado(fernando))
print(Estudiante.info(fernando))
print(Estudiante.agregar_nota(fernando,0))
print(Estudiante.info(fernando))
print(Estudiante.esta_aprobado(fernando))