class Actor:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.nacionalidad})"

    def __repr__(self):
        return f"Actor. ('{self.nombre}', {self.edad}, '{self.nacionalidad}')"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return NotImplemented
        return self.nombre == other.nombre and self.nacionalidad == other.nacionalidad

    def __lt__(self, other):
        if not isinstance(other, Actor):
            return NotImplemented
        return self.edad < other.edad

class Pelicula:
    def __init__(self, titulo, anio, valoracion, actores=None):
        self.titulo = titulo
        self.anio = anio
        self.valoracion = valoracion
        if actores is None:
            self.actores = []
        else:
            self.actores = actores

    def __str__(self):
        return f"{self.titulo} ({self.anio} - Valoración: {self.valoracion})"

    def __repr__(self):
        return f"Película('{self.titulo}', {self.anio}, {self.valoracion})"

    def __bool__(self):
        return self.valoracion >= 5

    def __eq__(self, other):
        if not isinstance(other, Pelicula):
            return NotImplemented
        return self.titulo == other.titulo and self.anio == other.anio

    def __add__(self, actor):
        if not isinstance(actor, Actor):
            return NotImplemented
        nuevos_actores = self.actores + [actor]
        return Pelicula(self.titulo, self.anio, self.valoracion, nuevos_actores)

    def __contains__(self, actor):
        return actor in self.actores

    def __len__(self):
        return len(self.actores)

    def __getitem__(self, indice):
        return self.actores[indice]

    def __iter__(self):
        return iter(self.actores)

    def media_edad(self):
        if len(self.actores) == 0:
            return 0
        return sum(actor.edad for actor in self.actores) / len(self.actores)

    def es_clasica(self):
        return 2026 - self.anio > 30

class Catalogo:

    def __init__(self, nombre):
        self.nombre = nombre
        self._peliculas = []

    def __len__(self):
        return len(self._peliculas)

    def __getitem__(self, indice):
        return self._peliculas[indice]

    def __iter__(self):
        return iter(self._peliculas)

    def __contains__(self, titulo):
        return any(pelicula.titulo == titulo for pelicula in self._peliculas)

    def __bool__(self):
        return len(self._peliculas) > 0

    def __eq__(self, other):
        if not isinstance:
            return NotImplemented
        return len(self) == len(other)

    def __add__(self, other):
        if not isinstance:
            return NotImplemented
        catalogo_nuevo = Catalogo(self.nombre + " - " + other.nombre)
        catalogo_nuevo._peliculas = self._peliculas + other._peliculas
        return catalogo_nuevo

    def __format__(self, format_spec):
        if format_spec == "titulos":
            titulos = ", ".join(pelicula.titulo for pelicula in self._peliculas)
            return f"[{self.nombre}]: {titulos}"
        return str(self)