# Ejercicio 1
class Perro:
  def hablar(self):
    return "Guau"

class Gato:
  def hablar(self):
    return "Miau"


animales = [Gato(),Perro()]
for animal in animales:
  print(animal.hablar())

# Ejercicio 2
class TarjetaCredito:
  def pagar(self,monto):
    return f"Se ha hecho un pago de {monto}€ con tarjeta de credito"

class Paypal:
  def pagar(self,monto):
    return f"Se ha hecho un pago de {monto}€ a traves de paypal"

class Efectivo:
  def pagar(self,monto):
    return f"Se ha hecho un pago de {monto}€ en efectivo"


metodos_de_pago = [TarjetaCredito(),Paypal(),Efectivo()]
for metodo in metodos_de_pago:
  print(metodo.pagar(30))

# Ejercicio 3
class Figura:
  def area(self):
    return f"El area es de 0"

class Rectangulo(Figura):
  def __init__(self,alto,ancho):
    self.alto = alto
    self.ancho = ancho

  def area(self):
    return f"El area del rectangulo es {self.ancho * self.alto}"

class Circulo(Figura):
  pi = 3.14
  def __init__(self,radio):
    self.radio = radio
  def area(self):
    return f"El area del circulo es {Circulo.pi * self.radio **2}"


figuras = [Figura(),Rectangulo(4,2), Circulo(5)]
for figura in figuras:
  print(figura.area())


# Ejercicio 4
class Pato:
  def sonido(self):
    return "El pato hace cuac"

class Persona:
  def sonido(self):
    return "hola, imito a un pato haciendo cuac"

def hacer_sonido(obj):
  return obj.sonido()

print(hacer_sonido(Pato()))
print(hacer_sonido(Persona()))

# Ejercicio 5
class Gerente:
  def reportar(self):
    return "Hola, soy un gerente y estoy gerenerando un reporte"

class Programador:
  def reportar(self):
    return "Hola, soy un programador y estoy gerenerando un reporte"

empleados = [Gerente(),Programador()]

for empleado in empleados:
  print(empleado.reportar())