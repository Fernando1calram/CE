"""class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1,2)
v2 = Vector(3,4)

print(v1 + v2)
print(v1 * 3)
print(-v1)"""

class Libro:

    # Representa un libro con título, autor y páginas

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def __repr__(self):
        return f"Libro {self.titulo}, {self.autor}, {self.paginas}"

    def __len__(self):
        return self.paginas

    def __bool__(self):
        return self.paginas > 0

class Biblioteca:

    # Colección de libros con acceso por índice, iteración, búsqueda y contexto

    def __init__(self, nombre):
        self.nombre = nombre
        self._libros = []

    # Contenedor: acceso por índice
    def __getitem__(self, key):
        return self._libros[key]

    # Iteración
    def __iter__(self):
        return iter(self._libros)

    # Longitud
    def __len__(self):
        return (len(self._libros))

    # Búsqueda con 'in'
    def __contains__(self, titulo):
        return any(l.titulo == titulo for l in self._libros)

    # Representación
    def __str__(self):
        return f"Biblioteca {self.nombre} {len(self)} libros"

    def __repr__(self):
        return f"Biblioteca {self.nombre}, libros={len(self)}"

    # Comparación por número de libros
    def __eq__(self, value):
        if not isinstance(value, Biblioteca):
            return NotImplemented
        return len(self) == len(value)

    def __lt__(self, other):
        if not isinstance(other, Biblioteca):
            return NotImplemented
        return len(self) < len(other)

    # Formato personalizado
    def __format__(self, format_spec):
        if format_spec == "resumen":
            titulos = ", ".join(l.titulo for l in self._libros)
            return f"{self.nombre}: {titulos}"
        return str(self)

    # Context manager: abre y cierra la biblioteca
    def __enter__(self):
        print(f">>> Abriendo biblioteca: {self.nombre}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"<<< Cerrando biblioteca: {self.nombre}")
        return False

    # Agregar libro
    def agregar(self, libro):
        self._libros.append(libro)

    # Obtener un libro por título (acceso por nombre)
    def obtener(self,titulo):
        return next((l for l in self._libros if l.titulo == titulo), None)

bib = Biblioteca("Ciencia Ficcion")
bib.agregar(Libro("Dune","Frank Herbert",412))
bib.agregar(Libro("Neuromante", "William Gibson", 271))
bib.agregar(Libro("Fundación", "Isaac Asimov", 255))

print(bib)
print(repr(bib))

print(f"Libros: {len(bib)}")

print(bib[0])
print(bib[1].paginas)

print("\nRecorriendo libros:")
for libro in bib:
    print(f" {libro}")

print(f"\n¿'Dune' en la biblioteca? {'Dune' in bib}")
print(f"\n¿'Matrix' en la biblioteca? {'Matrix' in bib}")

print(f"¿Biblioteca no vacía? {bool(bib)}")

bib_vacia = Biblioteca("Vacia")
print(f"¿Biblioteca vacía es falsa? {bool(bib_vacia)}")

# __format__ (f-string con formato personalizado)
print(f"\n{bib:resumen}")

bib2 = Biblioteca("Otra")
bib2.agregar(Libro("Libro único", "Autor X", 100))
print(f"\nlen(bib) == len(bib2) ? {bib == bib2}")
print(f"\nlen(bib) < len(bib2) ? {bib < bib2}")

# __enter__ / __exit__ (context manager)
print("\n--- Con context manager ---")
with Biblioteca("Biblioteca temporal") as b:
    b.agregar(Libro("Temporales","Alguien",50))
    print(f" Dentro: {b}")
print(" (Fuera del bloque)")