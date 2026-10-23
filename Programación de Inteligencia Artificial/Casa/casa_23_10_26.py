from abc import ABC, abstractmethod
from collections.abc import Iterator
from datetime import date
from math import sqrt


# Hereda de ABC para saber que es clase abstracta (define que debe saber hacer cualquier contenido recomendable)
class Recomendable(ABC):
    
    def __init__(self, titulo: str, valoracion: float) -> None: 
        # Atributos de todo contenido recomendable
        self.titulo = titulo
        self.valoracion = valoracion

    @abstractmethod
    def recomendacion(self) -> str:

        # No tiene implementación aquí y toda subclase está obligada a implementarla

        pass

    def etiqueta(self) -> str:
        # Las subclases lo heredan tal cual y usa el método abstracto recomendación (arriba)
        return f"Recomendación: {self.recomendacion()}"

class Pelicula(Recomendable):
    
    #Película concreta obligada a usar recomendacion()

    def __init__(self, titulo: str, anio: int, valoracion: float) -> None:
        super().__init__(titulo, valoracion)
        self.anio: int = anio

    def recomendacion(self) -> str:
        if(self.valoracion >= 8):
            return f"{self.titulo} es muy recomendable"
        return f"{self.titulo} es recomendable con reservas"

class Documental(Pelicula):

    # Hereda de película y añade un tema

    def __init__(self, titulo: str, anio: int, valoracion: float, tema: str) -> None:
        # Llamada al constructor de película
        super().__init__(titulo, anio, valoracion)
        self.tema: str = tema

    def recomendacion(self):
        # Podemos sobreescribir el método heredado
        if self.valoracion >= 8:
            return f"Muy recomendable si te interesa {self.tema}"
        return f"Interesante solo si te interesa mucho {self.tema}"

# Iteradores

class CatalogoPeliculas:

    # Catálogo que permite recorrer peliculas con for, next() o list comprehension

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self._peliculas: list[Pelicula] = []

    def agregar(self, pelicula: Pelicula) -> None:
        #Añade una película al catálogo
        self._peliculas.append(pelicula)

    def __len__(self) -> int:
        return len(self._peliculas)

    def __iter__(self):
        # Debe devolver un iterador
        # Usamos para ello CatalogoIterator, es la opción más clara si queremos que el catálogo sea iterable
        # y el iterador mantenga su propio estado
        return CatalogoIterator(self._peliculas)

    def mejores(self, minimo: float = 8.0) -> list[Pelicula]:
        return [pelicula for pelicula in self._peliculas if pelicula.valoracion >= minimo]

class CatalogoIterator:

    # Iterador personalizado para recorrer un catálogo

    def __init__(self, peliculas: list[Pelicula]) -> None:
        # Guardamos la lista de películas
        self._peliculas = peliculas

        # Posición actual del recorrido
        self._posicion = 0

    def __iter__(self) -> "CatalogoIterator":
        # Un iterador normalmente se devuelve a sí mismo
        return self

    def __next__(self) -> Pelicula:
        # Devuelve la siguiente película
        # Si no quedan películas lanza StopIteration que hace que el bucle for termine
        if self._posicion >= len(self._peliculas):
            raise StopIteration
        pelicula = self._peliculas[self._posicion]
        self._posicion += 1

        return pelicula
    
# ============================================================
# PRUEBAS
# ============================================================

print("=" * 55)
print("  PRUEBAS DE CLASES ABSTRACTAS E ITERADORES")
print("=" * 55)

# ── Clases abstractas ──
print("\n--- Clases abstractas ---")
pelicula = Pelicula("El Padrino", 1972, 9.2)
documental = Documental("Planeta Tierra", 2006, 9.5, "naturaleza")

# Ambos objetos son Recomendable.
assert isinstance(pelicula, Recomendable)
assert isinstance(documental, Recomendable)

# Cada clase implementa recomendacion() a su manera.
print(f"  {pelicula.etiqueta()}")
print(f"  {documental.etiqueta()}")

assert "muy recomendable" in pelicula.recomendacion().lower()
assert "naturaleza" in documental.recomendacion().lower()
print("  Clases abstractas ✓")

# ── Una clase abstracta no se puede instanciar ──
print("\n--- Instanciar clase abstracta ---")
try:
    # Esto debe fallar porque Recomendable es abstracta.
    objeto = Recomendable("Prueba", 7.0)
except TypeError as error:
    print(f"  Error esperado: {error}")

# ── Iteradores ──
print("\n--- Iteradores ---")
catalogo = CatalogoPeliculas("Cine recomendado")

catalogo.agregar(pelicula)
catalogo.agregar(documental)
catalogo.agregar(Pelicula("Película regular", 2020, 6.5))

# len() usa __len__.
assert len(catalogo) == 3

# El for usa __iter__() y después __next__().
titulos = [pelicula.titulo for pelicula in catalogo]
assert titulos == ["El Padrino", "Planeta Tierra", "Película regular"]
print(f"  Películas recorridas: {titulos}")

# También podemos usar un iterador manualmente.
iterador = iter(catalogo)

primera = next(iterador)
segunda = next(iterador)
tercera = next(iterador)

assert primera.titulo == "El Padrino"
assert segunda.titulo == "Planeta Tierra"
assert tercera.titulo == "Película regular"

# Al no quedar más elementos, next() lanza StopIteration.
try:
    next(iterador)
except StopIteration:
    print("  StopIteration controlada correctamente ✓")