class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock}"

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock})"

    def __bool__(self):
        if self.stock == 0:
            return False
        else:
            return True

    def __mul__(self, other):
        return self.precio * other

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self._productos = []

    def __len__(self):
        return len(self.nombre)

    def __getitem__(self, key):
        return self._productos[key]

    def __iter__(self):
        return iter(self._productos)

    def __contains__(self, item):
        return any(p.nombre == item for p in self._productos)

    def __str__(self):
        return f"Tienda: {self.nombre} {len(self)} productos"

    def __repr__(self):
        return f"Tienda: {self.nombre}, productos {len(self)}"

    def __bool__(self):
        if self:
            return True
        else:
            return False

    def __eq__(self, value):
        if not isinstance(value, Tienda):
            return NotImplemented
        return len(self) == len(value)

    def __format__(self, format_spec):
        if format_spec == "inventario":
            productos = ", ".join(p for p in self._productos)
            return f"{self.nombre}: {productos}"
        return str(self)

    def __add__(self, other):
        tienda_nueva = Tienda({self.nombre + other.nombre})
        tienda_nueva._productos = self._productos.append(other._productos)
        return tienda_nueva

    def __enter__(self):
        print(f" >>> Abriendo tienda: {self.nombre}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"<<< Cerrando tienda: {self.nombre}")
        return self

    def agregar(self, producto):
        return self._productos.append(producto)

    def buscar(self, nombre):
        return next((p for p in self._productos if p.nombre == nombre), None)

    def total(self):
        for p in self._productos:
            print(f"{p.nombre} tenemos {p.cantidad}, cada uno cuesta: {p.precio}. Total: {p.cantidad * p.precio}")

# PRUEBAS

# Crear tienda y agregar productos
print("=" * 55)
print("  PRUEBAS DE LA CLASE TIENDA")
print("=" * 55)

# ── Crear tienda y agregar productos ──
tienda = Tienda("ElectroMundo")
tienda.agregar(Producto("Laptop", 999.99, 10))
tienda.agregar(Producto("Ratón", 19.99, 50))
tienda.agregar(Producto("Teclado", 49.99, 0))  # stock 0


# ── assert: __len__ ──
print("\n--- __len__ ---")
assert len(tienda) == 3, f"len(tienda) = {len(tienda)}, esperado 3"
print(f"  len(tienda) = {len(tienda)}  ✓")

"""
# ── assert: __getitem__ ──
print("\n--- __getitem__ ---")
assert tienda[0].nombre == "Laptop", f"tienda[0].nombre = {tienda[0].nombre}"
assert tienda[1].precio == 19.99, f"tienda[1].precio = {tienda[1].precio}"
print(f"  tienda[0].nombre = '{tienda[0].nombre}'  ✓")
print(f"  tienda[1].precio = {tienda[1].precio}  ✓")

# ── assert: __iter__ ──
print("\n--- __iter__ ---")
nombres = [p.nombre for p in tienda]
assert nombres == ["Laptop", "Ratón", "Teclado"], f"nombres = {nombres}"
print(f"  nombres = {nombres}  ✓")

# ── assert: __contains__ ──
print("\n--- __contains__ ---")
assert "Laptop" in tienda, "'Laptop' no se encontró en tienda"
assert "Monitor" not in tienda, "'Monitor' debería estar fuera"
print(f"  'Laptop' in tienda = True  ✓")
print(f"  'Monitor' not in tienda = True  ✓")

# ── assert: __bool__ ──
print("\n--- __bool__ (tienda) ---")
assert bool(tienda) is True, f"bool(tienda) = {bool(tienda)}"
tienda_vacia = Tienda("Vacia")
assert bool(tienda_vacia) is False, f"bool(tienda_vacia) = {bool(tienda_vacia)}"
print(f"  bool(tienda) = True  ✓")
print(f"  bool(tienda_vacia) = False  ✓")

# ── assert: __str__ y __repr__ ──
print("\n--- __str__ y __repr__ ---")
print(f"  str:  {tienda}")
print(f"  repr: {repr(tienda)}")

# ── assert: __format__ ──
print("\n--- __format__ ---")
resultado_fmt = f"{tienda:inventario}"
print(f"  {resultado_fmt}")
assert "[ElectroMundo]" in resultado_fmt, f"formato incorrecto: {resultado_fmt}"

# ── assert: __eq__ ──
print("\n--- __eq__ ---")
tienda2 = Tienda("Otra")
tienda2.agregar(Producto("Auriculares", 29.99, 5))
# FIX: tienda tiene 3 productos, tienda2 tiene 1.
# Para que tienda == tienda2, tienda2 debe tener 3 productos.
tienda2.agregar(Producto("Monitor", 200.0, 3))
tienda2.agregar(Producto("Cable", 5.99, 100))
assert tienda == tienda2, f"len(tienda)={len(tienda)}, len(tienda2)={len(tienda2)}"
print(f"  len(tienda) == len(tienda2) ({len(tienda)} == {len(tienda2)})  ✓")

# ── assert: __add__ ──
print("\n--- __add__ ---")
combinada = tienda + tienda2
assert len(combinada) == 6, f"len(combinada) = {len(combinada)}, esperado 6"
print(f"  len(combinada) = {len(combinada)}  ✓")

# ── assert: __bool__ (producto sin stock) ──
print("\n--- __bool__ (producto) ---")
assert bool(Producto("Viejo", 1.0, 0)) is False, "Producto sin stock debería ser False"
print(f"  bool(Producto sin stock) = False  ✓")

# ── assert: __mul__ ──
print("\n--- __mul__ ---")
resultado_mul = Producto("Laptop", 999.99, 10) * 3
assert abs(resultado_mul - 2999.97) < 0.01, f"precio × 3 = {resultado_mul}, esperado ~2999.97"
print(f"  3 Laptops cuestan: {resultado_mul:.2f}€  ✓")

# ── assert: context manager ──
print("\n--- Context manager ---")
with Tienda("Temporal") as t:
    t.agregar(Producto("Temporal", 5.0, 1))
    assert len(t) == 1, f"len(t) = {len(t)}, esperado 1"
    print(f"  len(t) = {len(t)}  ✓")

print("\n" + "=" * 55)
print("  ¡TODAS LAS PRUEBAS PASADAS!")
print("=" * 55)"""