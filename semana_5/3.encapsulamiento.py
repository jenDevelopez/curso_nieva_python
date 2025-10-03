# Ejercicio 1
class CuentaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo


  @property
  def saldo(self):
    return self.__saldo

  def depositar(self, cantidad):
    if cantidad < 0:
      print("Debes depositar una cantidad mayor que 0")
    else:
      self.__saldo += cantidad

  def retirar(self,cantidad):
    if cantidad > self.__saldo:
      print(f"No tienes suficiente saldo. Tu saldo actual es {self.__saldo}")
    else:
      self.__saldo -= cantidad

bbva = CuentaBancaria(500)
print(bbva.saldo)
bbva.depositar(300)
print(bbva.saldo)
bbva.retirar(1000)
print(bbva.saldo)
bbva.retirar(200)
print(bbva.saldo)

# Ejercicio 2
class Usuario:
  def __init__(self, username: str, email:str):
    self.username = username
    self._email = None
    self.email = email

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, valor:str):
    if '@' not in valor or '.' not in valor.split('@')[-1]:
      raise ValueError("Email invalido (formato simple)")
    self._email = valor

u1 = Usuario('user1','usuario@usuario.es')
print(u1.username, u1.email)

# Ejercicio 3
class Producto:

  iva = 0.16
  def __init__(self,precio):
    self.__precio = precio

  @property
  def precio(self):
    return self.__precio

  @precio.setter
  def precio(self,precio):
    self.__precio = precio



  def __str__(self):
    return f"El precio con iva es {self.__precio * (1 + Producto.iva)}"

p1 = Producto(10)
print(p1)

# Ejercicio 4
class Vehiculo:
  def __init__(self,odometro):
    self.__odometro = odometro


  @property
  def odometro(self):
    return self.__odometro

  @odometro.setter
  def odometro(self,valor):
    if valor < self.__odometro:
      raise ValueError(f"el valor debe ser mayor al valor actual de odometro, el valor actual es {self.__odometro}")
    else:
      self.__odometro = valor

  def recorrer(self):
    if self.__odometro > 0:
      self.__odometro += 1


v = Vehiculo(5)
print(v.odometro)
v.recorrer()
print(v.odometro)

# Ejercicio 5
'''
Implementa RegistroTemperatura
con lista interna privada __mediciones. Expón:

agregar(valor) para añadir mediciones (float).
Propiedad de solo lectura promedio.
Propiedad mediciones que devuelva una tupla
(copia segura) para no permitir modificaciones externas.
'''

class RegistroTemperatura:
  def __init__(self):
    self.__mediciones = []

  def agregar(self,valor:float):
    self.__mediciones.append(float(valor))

  @property
  def promedio(self):
    if not self.__mediciones:
      return 0.0
    return sum(self.__mediciones) / len(self.__mediciones)

  @property
  def mediciones(self):
    return tuple(self.__mediciones)


tmp = RegistroTemperatura()
tmp.agregar(37.0)
tmp.agregar(21.5)
tmp.mediciones
tmp.promedio

# Ejercicio 6
class Carrito:

  def __init__(self):
    self.__items = {}

  def agregar(self, sku:str, precio:float, cantidad: int = 1):
    if precio <= 0 or cantidad <= 0:
      raise ValueError('Precio y cantidad deben ser mayores a 0')
    if sku not in self.__items:
      self.__items[sku] = {'precio':float(precio),'cantidad':int(cantidad)}
    else:
      self.__items[sku]['precio'] = float(precio)
      self.__items[sku]['cantidad'] = int(precio)

  def  quitar(self,sku:str,cantidad:int = 1):
    if sku not in self.__items:
      raise KeyError(f"SKU no encontrado: {sku}")
    if cantidad <= 0:
      raise ValueError('Cantidad debe ser mayor que 0')
    self.__items[sku]["cantidad"] -= int(cantidad)
    if self.__items[sku]["cantidad"] <= 0:
      del self.__items[sku]

  @property
  def total(self):
    return sum(d["precio"] * d["cantidad"] for d in self.__items.values())


  @property
  def items(self):
      return {sku:data.copy() for sku, data in self.__items.items()}


car = Carrito()
car.agregar("ABC123", 100.0, 2)
car.agregar("XYZ999", 50.0, 1)
car.quitar("ABC123", 1)
car.total
car.items
 # {'ABC123': {'precio': 100.0, 'cantidad': 1}, 'XYZ999': {'precio': 50.0, 'cantidad': 1}}
 # 150.0