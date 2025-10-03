# Ejercicio 1
class Usuario:
  def __init__(self, username,email, activo=True):
    self.username = username
    self.email = email
    self.activo = activo

  def info(self):
    state = "Activo" if self.activo == True else "Inactivo"
    print(f"Nombre de usuario {self.username}")
    print(f"Email del usuario {self.email}")
    print(f"Estado: {state}")


user1 = Usuario('user1','user1@gmail.com')
user2 = Usuario('user2','user2@gmail.com',False)
user1.info()
user2.info()

# Ejercicio 2
class Producto:
  def __init__(self, nombre, precio, cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad

  def subtotal(self):
    return self.precio * self.cantidad


laptops = Producto('latop Acer',800,15)
total_laptops = laptops.subtotal()
print(total_laptops)

# Ejercicio 3
class Transaccion:
  def __init__(self, monto, tipo, description=''):
    if tipo not in('deposito', 'retiro'):
      raise ValueError('Tipo invalido')
    self.monto = monto
    self.tipo = tipo
    self.description = description


transaccion1 = Transaccion(500,'retiro','Ingreso a mi cuenta')
print(transaccion1.monto)
print(transaccion1.tipo)


# Ejercicio 4
from datetime import date
class Proyecto:
  def __init__(self, nombre, responsable, fecha_inicio=None):
    self.nombre = nombre
    self.responsable = responsable
    self.fecha_inicio = fecha_inicio or date.today()


proyecto1 = Proyecto('blog con django','Jennifer')
print(proyecto1.nombre, proyecto1.responsable, proyecto1.fecha_inicio)


# Ejercicio5
class Grupo:
  def __init__(self, nombre, lista_miembros=None):
    self.nombre = nombre
    self.lista_miembros = lista_miembros or []

  def agregar(self, miembro):
    self.lista_miembros.append(miembro)


grupo1 = Grupo('Grupo de lectura')
print(grupo1.lista_miembros)
grupo1.agregar('charlotte')
print(grupo1.lista_miembros)