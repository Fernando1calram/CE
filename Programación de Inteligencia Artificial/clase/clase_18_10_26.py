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

    def __enter__(self):
        print(f">>> Abriendo catálogo: {self.nombre}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"<<< Cerrando catálogo: {self.nombre}")

    def agregar(self, pelicula):
        self._peliculas.append(pelicula)

    def buscar(self, titulo):
        return next((pelicula for pelicula in self._peliculas if pelicula.titulo == titulo),
                    None)

    def mejores(self, minimo=8):
        return [pelicula for pelicula in self._peliculas if pelicula.valoracion >= minimo]

# ============================================================
# PRUEBAS
# ============================================================
# Los assert comprueban condiciones.
#
#   assert condicion
#
# Si la condición es True, el programa continúa.
# Si es False, Python lanza un AssertionError.
# ============================================================

print("=" * 55)
print("  PRUEBAS DE PELÍCULAS, ACTORES Y CATÁLOGO")
print("=" * 55)

# ── Creamos varios actores ──
# Cada llamada a Actor() ejecuta __init__.
print("\n--- Actores ---")
marlon = Actor("Marlon Brando", 80, "Estados Unidos")
al = Actor("Al Pacino", 84, "Estados Unidos")
penelope = Actor("Penélope Cruz", 52, "España")
javier = Actor("Javier Bardem", 57, "España")

# Comprobamos que __init__ guardó bien los atributos.
assert marlon.nombre == "Marlon Brando"
assert al.edad == 84
assert penelope.nacionalidad == "España"

# Aquí se ejecuta __str__.
print(f"  {marlon}")
print(f"  {al}")
print("  Creación de actores ✓")

# ── Comprobamos __eq__ de Actor ──
# Dos actores con el mismo nombre y nacionalidad son iguales.
print("\n--- Actor.__eq__ ---")
marlon_copia = Actor("Marlon Brando", 80, "Estados Unidos")

assert marlon == marlon_copia
assert marlon != al
print("  Comparación de actores ✓")

# ── Comprobamos __lt__ y la ordenación ──
# sorted() necesita que los objetos sepan compararse con <.
print("\n--- Actor.__lt__ ---")
actores_ordenados = sorted([al, marlon, penelope, javier])
edades = [actor.edad for actor in actores_ordenados]

# Las edades deben quedar ordenadas de menor a mayor.
assert edades == sorted(edades)
print(f"  Edades ordenadas: {edades} ✓")

# ── Creamos películas ──
# Cada llamada a Pelicula() ejecuta __init__.
print("\n--- Películas ---")
padrino = Pelicula("El Padrino", 1972, 9.2, [marlon, al])
abre_los_ojos = Pelicula("Abre los ojos", 1997, 7.8, [penelope])
pelicula_mala = Pelicula("Película mala", 2020, 3.5)

# Comprobamos los atributos básicos.
assert padrino.titulo == "El Padrino"
assert padrino.anio == 1972

# len(padrino) ejecuta __len__.
assert len(padrino) == 2

# print(padrino) ejecuta __str__.
print(f"  {padrino}")
print(f"  Número de actores: {len(padrino)} ✓")

# ── Comprobamos __bool__ de Pelicula ──
# Una película con valoración menor que 5 debe ser False.
print("\n--- Pelicula.__bool__ ---")
assert bool(padrino) is True
assert bool(pelicula_mala) is False
print("  Valoración booleana de películas ✓")

# ── Comprobamos __contains__ ──
# marlon in padrino ejecuta Pelicula.__contains__.
print("\n--- Pelicula.__contains__ ---")
assert marlon in padrino
assert penelope not in padrino
print("  Búsqueda de actores en película ✓")

# ── Comprobamos __getitem__ e __iter__ ──
# pelicula[0] ejecuta __getitem__.
# El bucle for ejecuta __iter__.
print("\n--- Pelicula.__getitem__ e __iter__ ---")
assert padrino[0].nombre == "Marlon Brando"
assert padrino[-1].nombre == "Al Pacino"

nombres_actores = [actor.nombre for actor in padrino]
assert nombres_actores == ["Marlon Brando", "Al Pacino"]
print(f"  Actores: {nombres_actores} ✓")

# ── Comprobamos __add__ ──
# padrino + javier ejecuta Pelicula.__add__.
print("\n--- Pelicula.__add__ ---")
pelicula_ampliada = padrino + javier

# La nueva película debe tener 3 actores.
assert len(pelicula_ampliada) == 3

# La película original no debe haber cambiado.
assert len(padrino) == 2

# Javier debe estar en la nueva película.
assert javier in pelicula_ampliada
print("  Unión inmutable de actor a película ✓")

# ── Comprobamos media_edad ──
# Método normal: calcula la edad media de los actores.
print("\n--- Pelicula.media_edad ---")
media = padrino.media_edad()

# Marlon tiene 80 años y Al 84: la media es 82.
assert abs(media - 82) < 0.01

# Una película sin actores debe devolver 0.
assert Pelicula("Sin actores", 2024, 7).media_edad() == 0
print(f"  Media de edad: {media} ✓")

# ── Comprobamos es_clasica ──
# Método normal: comprueba si la película tiene más de 30 años.
print("\n--- Pelicula.es_clasica ---")
assert padrino.es_clasica() is True
assert pelicula_mala.es_clasica() is False
print("  Detección de películas clásicas ✓")

# ── Creamos y probamos el catálogo ──
print("\n--- Catálogo ---")
catalogo = Catalogo("Cine clásico")

# agregar() añade películas a la lista interna.
catalogo.agregar(padrino)
catalogo.agregar(abre_los_ojos)
catalogo.agregar(pelicula_mala)

# len(catalogo) ejecuta __len__.
assert len(catalogo) == 3

# catalogo[0] ejecuta __getitem__.
assert catalogo[0].titulo == "El Padrino"

# "El Padrino" in catalogo ejecuta __contains__.
assert "El Padrino" in catalogo
assert "Titanic" not in catalogo

# bool(catalogo) ejecuta __bool__.
assert bool(catalogo) is True

# print(catalogo) ejecuta __str__.
print(f"  {catalogo}")
print("  Catálogo creado correctamente ✓")

# ── Comprobamos buscar ──
# Método normal: busca por título y devuelve la película o None.
print("\n--- Catalogo.buscar ---")
encontrada = catalogo.buscar("Abre los ojos")

assert encontrada is not None
assert encontrada.titulo == "Abre los ojos"
assert catalogo.buscar("Titanic") is None
print("  Búsqueda de películas ✓")

# ── Comprobamos mejores ──
# Método normal: filtra películas por valoración mínima.
print("\n--- Catalogo.mejores ---")
mejores = catalogo.mejores(8)
titulos_mejores = [pelicula.titulo for pelicula in mejores]

assert titulos_mejores == ["El Padrino"]
print(f"  Mejores películas: {titulos_mejores} ✓")

# ── Comprobamos __eq__ de Catalogo ──
# catalogo == catalogo2 ejecuta Catalogo.__eq__.
print("\n--- Catalogo.__eq__ ---")
catalogo2 = Catalogo("Otro catálogo")

catalogo2.agregar(Pelicula("A", 2000, 6))
catalogo2.agregar(Pelicula("B", 2001, 6))
catalogo2.agregar(Pelicula("C", 2002, 6))

assert catalogo == catalogo2
print(f"  len(catalogo) == len(catalogo2) ({len(catalogo)} == {len(catalogo2)}) ✓")

# ── Comprobamos __add__ de Catalogo ──
# catalogo + catalogo2 ejecuta Catalogo.__add__.
print("\n--- Catalogo.__add__ ---")
catalogo_combinado = catalogo + catalogo2

# 3 películas + 3 películas = 6 películas.
assert len(catalogo_combinado) == 6
print(f"  Catálogo combinado: {len(catalogo_combinado)} películas ✓")

# ── Comprobamos __format__ ──
# f"{catalogo:titulos}" ejecuta __format__ con format_spec = "titulos".
print("\n--- Catalogo.__format__ ---")
formato = f"{catalogo:titulos}"

print(f"  {formato}")
assert "[Cine clásico]" in formato
assert "El Padrino" in formato
print("  Formato personalizado ✓")

# ── Comprobamos el context manager ──
# with ejecuta __enter__ al entrar y __exit__ al salir.
print("\n--- Context manager ---")
with Catalogo("Catálogo temporal") as c:
    c.agregar(Pelicula("Temporal", 2026, 8))

    # Comprobamos que __enter__ devolvió el propio catálogo.
    assert len(c) == 1
    print(f"  Películas en catálogo temporal: {len(c)} ✓")

print("\n" + "=" * 55)
print("  ¡TODAS LAS PRUEBAS PASADAS!")
print("=" * 55)
              