# Ejercicio 1
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad


p1 = Persona('Alfredo',52)
p2 = Persona('Alana',25)
print(p1.nombre, p1.edad)
print(p2.nombre, p2.edad)

# Ejercicio 2
class Producto:
  impuesto = 0.16
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

pr1 = Producto('laptop',1200)
pr2 = Producto('Queso rallado',1)
print(f"El precio del producto con impuesto es {pr1.nombre} {pr1.precio + pr1.precio * Producto.impuesto}")
print(f"El precio del producto con impuesto es {pr2.nombre} {pr2.precio + pr2.precio * Producto.impuesto}")

# Ejercicio 3

class Rectangulo:
  def __init__(self,ancho, alto):
    self.ancho = ancho
    self.alto = alto

  def area(self):
    return self.alto * self.ancho


r1 = Rectangulo(5,7)
r2 = Rectangulo(18,2)
r3 = Rectangulo(85,36)
print(r1.area(), r2.area(), r3.area())

# Ejercicio 4
class Usuario:
  contador = 0

  def __init__(self, nombre):
    self.nombre = nombre
    Usuario.contador += 1


  @classmethod
  def total_usuarios(cls):
    if cls.contador == 1:
      return f"Se ha creado {cls.contador} usuario"
    else:
      return f"Se han creado {cls.contador} usuarios"

u1 = Usuario('Alicia')
print(Usuario.total_usuarios())
u2 = Usuario('Martin')
print(Usuario.total_usuarios())

# Ejercicio 5
class Matematicas:
  @staticmethod
  def es_par(n):
    return True if n % 2 == 0 else False


m1 = Matematicas()
print(m1.es_par(2))
print(m1.es_par(3))
print(m1.es_par(1548452))

# Ejercicio 6
class Libro:
  def __init__(self,titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def __str__(self):
    return f" Titulo: {self.titulo} | Autor: {self.autor}"

l1 = Libro('Hatty Potter: La piedra filosofal','JK Rowling')
print(l1)