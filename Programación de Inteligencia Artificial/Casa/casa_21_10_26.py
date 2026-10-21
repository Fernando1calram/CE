# 1.6
from datetime import date

class Identificable:

    def __init__(self, id_objeto: int) -> None:
        self.id_objeto = id_objeto

    def identificar(self) -> str:
        return f"ID: {self.id_objeto}"

class Valorable:

    def __init__(self, valoracion: float) -> None:
        self.valoracion = valoracion

    def mostrar_valoracion(self) -> str:
        return f"Valoración: {self.valoracion}/10"

class ContenidoAudiovisual(Identificable, Valorable):

    def __init__(self, id_objeto: int, titulo,  valoracion: float) -> None:
        Identificable.__init__(self, id_objeto)
        Valorable.__init__(self, valoracion)

        self.titulo = titulo

    def descripcion(self) -> str:
        return f"{self.titulo} | {self.identificar()} | {self.mostrar_valoracion()}"

"""print("MRO de COntenidoAudiovisual")
for clase in ContenidoAudiovisual.mro():
    print(f"  - {clase.__name__}")"""

# 1.7
class Actor:

    def __init__(self, nombre: str, edad: int, nacionalidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nacionalidad: str = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.nacionalidad})"

class Pelicula(ContenidoAudiovisual):

    def __init__(self, id_objeto: int, titulo: str, anio: int, valoracion: float, actores: list[Actor] | None = None):
        super().__init__(id_objeto, titulo, valoracion)

        self.anio: int = anio

        self.actores: list[Actor] = actores if actores is not None else[]

    def agregar_actor(self, actor: Actor) -> None:
        self.actores.append(actor)

    def buscar_actor(self, nombre: str) -> Actor | None:
        for actor in self.actores:
            if actor.nombre == nombre:
                return actor
        return None

    def media_edad(self) -> float:
        if not self.actores:
            return 0.0
        return sum(actor.edad for actor in self.actores) / len(self.actores)

# 1.8
class Serie(ContenidoAudiovisual):

    plataforma: str = "Genérica"

    def __init__(self, id_objeto: int, titulo: str, valoracion: float, temporadas: int) -> None:
        super().__init__(id_objeto, titulo, valoracion)

        self._temporadas: int = temporadas

    @property
    def temporadas(self) -> int:
        return self._temporadas

    @temporadas.setter
    def temporadas(self, valor: int) -> None:
        if valor < 1:
            raise ValueError("Una serie debe tener al menos una temporada.")
        self._temporadas = valor

    @property
    def es_larga(self) -> bool:
        return self._temporadas >= 5

    @staticmethod
    def es_estreno(anio) -> bool:
        return anio >= date.today().year

    @classmethod
    def desde_titulo(cls, titulo: str, valoracion: float = 7.0) -> "Serie":
        return cls(id_objeto = 999, titulo = titulo, valoracion = valoracion, temporadas = 1)


# ============================================================
# PRUEBAS
# ============================================================

print("\n" + "=" * 55)
print("  PRUEBAS DE HERENCIA, TYPE HINTS Y DECORADORES")
print("=" * 55)

# ── Herencia múltiple ──
print("\n--- Herencia múltiple ---")
pelicula = Pelicula(
    id_objeto=1,
    titulo="El Padrino",
    anio=1972,
    valoracion=9.2,
)

# pelicula hereda identificar() de Identificable.
# pelicula hereda mostrar_valoracion() de Valorable.
print(f"  {pelicula.descripcion()}")

# Comprobamos que hereda de las dos clases.
assert isinstance(pelicula, Identificable)
assert isinstance(pelicula, Valorable)
print("  Herencia múltiple ✓")

# ── Type hints ──
print("\n--- Type hints ---")
marlon = Actor("Marlon Brando", 80, "Estados Unidos")
al = Actor("Al Pacino", 84, "Estados Unidos")

pelicula.agregar_actor(marlon)
pelicula.agregar_actor(al)

# buscar_actor devuelve Actor | None.
encontrado = pelicula.buscar_actor("Al Pacino")
no_encontrado = pelicula.buscar_actor("Penélope Cruz")

assert encontrado is not None
assert encontrado.nombre == "Al Pacino"
assert no_encontrado is None

# media_edad devuelve float.
assert abs(pelicula.media_edad() - 82.0) < 0.01
print(f"  Media de edad: {pelicula.media_edad()} ✓")

# ── @property ──
print("\n--- @property ---")
serie = Serie(
    id_objeto=2,
    titulo="Dark",
    valoracion=8.8,
    temporadas=3,
)

# Leemos como si fuera un atributo,
# pero realmente se ejecuta el getter.
print(f"  Temporadas: {serie.temporadas}")
print(f"  ¿Es larga?: {serie.es_larga}")

assert serie.temporadas == 3
assert serie.es_larga is False

# Asignamos un valor: se ejecuta el setter.
serie.temporadas = 6

assert serie.temporadas == 6
assert serie.es_larga is True
print("  Property con getter y setter ✓")

# ── Validación en el setter ──
print("\n--- Validación en @property ---")
try:
    serie.temporadas = 0
except ValueError as error:
    print(f"  Error controlado: {error}")

# ── @staticmethod ──
print("\n--- @staticmethod ---")
# Se puede llamar desde la clase sin crear un objeto.
print(f"  ¿1972 es estreno?: {Serie.es_estreno(1972)}")
print(f"  ¿2026 es estreno?: {Serie.es_estreno(2026)}")

assert Serie.es_estreno(1972) is False
assert Serie.es_estreno(2026) is True
print("  staticmethod ✓")

# ── @classmethod ──
print("\n--- @classmethod ---")
serie_alternativa = Serie.desde_titulo("Stranger Things")

# desde_titulo es un constructor alternativo.
assert isinstance(serie_alternativa, Serie)
assert serie_alternativa.titulo == "Stranger Things"
assert serie_alternativa.temporadas == 1
print(f"  Serie creada: {serie_alternativa.titulo} ✓")

print("\n" + "=" * 55)
print("  ¡TODAS LAS PRUEBAS PASADAS!")
print("=" * 55)