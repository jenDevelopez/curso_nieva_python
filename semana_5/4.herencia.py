# Ejercicio 1
class Transporte:
  def __init__(self, capacidad, velocidad):
    self.capacidad = capacidad
    self.velocidad = velocidad

class Avion(Transporte):
  def __init__(self, capacidad, velocidad):
    super().__init__(capacidad,velocidad)

  def info(self):
    return f"El avion tiene una capacidad de {self.capacidad} y una velocidad de {self.velocidad} km/h"


class Barco(Transporte):
  def __init__(self, capacidad, velocidad):
    super().__init__(capacidad,velocidad)

  def info(self):
    return f"El barco tiene una capacidad de {self.capacidad} y una velocidad de {self.velocidad} nudos"

a = Avion(100,900)
b = Barco(300,70)
print(a.info())
print(b.info())

class Producto:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio


class Alimento(Producto):
  def __init__(self, nombre, precio, caducidad):
    super().__init__(nombre,precio)
    self.caducidad = caducidad

  def detalle(self):
    return f"Nombre de producto: {self.nombre} \nPrecio: {self.precio} \nFecha de caducidad: {self.caducidad}"

class Electrodomestico(Producto):
  def __init__(self, nombre, precio, garantia):
    super().__init__(nombre, precio)
    self.garantia = garantia

  def detalle(self):
    return f"Nombre de electrodomestico: {self.nombre} \nPrecio: {self.precio} \nFin de garantia: {self.garantia}"

a = Alimento('lomo de cerdo', 4.94, '25-09-2025')
print(a.detalle())
e = Electrodomestico('Lavadora',300.00,'05-02-2030')
print(e.detalle())

# Ejercicio 3
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad


class Profesor(Persona):
  def __init__(self, nombre, edad, materia):
    super().__init__(nombre, edad)
    self.materia = materia

  def presentarse(self):
    return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy profesor de {self.materia}"


class Estudiante(Persona):
  def __init__(self, nombre, edad, carrera):
    super().__init__(nombre, edad)
    self.carrera = carrera

  def presentarse(self):
    return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"

p = Profesor('Luis',45,'Matemáticas')
e = Estudiante('Mararena',20,'Arquitectura')
print(p.presentarse())
print(e.presentarse())