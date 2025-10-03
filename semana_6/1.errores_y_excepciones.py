# Ejercicio 1
def a_entero(texto:str):
  try:
    return int(texto)
  except:
    print('Entrada invalida')
    return None

a_entero("42")
a_entero("cuarenta")
a_entero("3.14")


# Ejercicio 2
def item_en(lista,i):
  try:
    return lista[i]
  except IndexError:
    print('Indice fuera de rango')
    return None



item_en([1,2,3], 1)
item_en([1,2,3], 5)
item_en([1,2,3], -4)

# Ejercicio 3
def leer_edad(usuario:dict):
  try:
    return int(usuario["edad"])
  except KeyError:
    print('Falta edad')
    return None
  except ValueError:
    print('Edad invalida')
    return None
leer_edad({"edad":"30"})
leer_edad({})
leer_edad({"edad":"treinta"})

# Ejercicio 4
def suma_segura(a,b):
  try:
    return float(a) + float(b)
  except ValueError:
    print('Dato invalido')
    return None
  else:
    print('OK')
  finally:
    print('Hecho')

suma_segura("2", "3.5")
suma_segura("2", "x")

# Ejercicio 5
def retirar(saldo:int, monto:int):
  if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser numérico.")
  if monto <= 0:
      raise ValueError("El monto debe ser positivo.")
  if monto > saldo:
      raise ValueError(f"Fondos insuficientes: saldo={saldo}, monto={monto}.")
  return saldo - monto

retirar(100, 40)
# retirar(100, "20")

# Ejercicio 6
def email_LBYL(usuario):
  if "email" in usuario:
    return usuario["email"]
  else:
    return "No se encuentra la propiedad email"

def email_EAFP(usuario):
  try:
    return usuario["email"]
  except KeyError:
    print("No se encuentra la clave email en usuario")

email_LBYL({"email":"a@b.com"})
email_LBYL({"nombre":"Ana"})
email_EAFP({"email":"a@b.com"})
email_EAFP({})

# Ejercicio 7
def leer_texto(ruta):
  file = None
  try:
    file = open(ruta,"r",encoding="utf-8")
    content = file.read()
    print('Archivo abierto')
    return content
  except FileNotFoundError:
    print("No encontrado")
    return ""
  except PermissionError:
    print("Sin permiso")
    return ""
  finally:
    if file is not None:
      file.close()

leer_texto("noexiste.txt")
leer_texto("datos.txt")


# Ejercicio 8
import json
import logging
logging.basicConfig(level=logging.INFO)

def cargar_config(ruta):
  try:
    with open(ruta, "r", encoding="utf-8") as f:
      return json.load(f)
  except FileNotFoundError as e:
    raise RuntimeError("Config ausente") from e
  except json.JSONDecodeError:
    logging.exception("Config invalida")
    raise

cargar_config("noexiste.json")

# Ejercicio 9
class InventarioError(Exception):
  '''Error general del inventario'''

class ProductoNoEncontrado(InventarioError):
  def __init__(self,sku):
    super().__init__(f"Producto '{sku}' no encontrado")
    self.sku = sku


class StockInsuficiente(InventarioError):
  def __init__(self,sku,solicitado, disponible):
    super().__init__(f"Stock insuficiente para '{sku}' solicitado={solicitado}, disponible={disponible}")
    self.sku = sku
    self.solicitado = solicitado
    self.disponible = disponible


def vender(inventario, sku, unidades):
  if unidades <= 0:
    raise ValueError('Las unidades deben ser positivas')

  try:
    prod = inventario[sku]
  except KeyError as e:
    raise ProductoNoEncontrado from e


  if unidades > prod["cantidad"]:
    raise StockInsuficiente(sku, unidades, prod["cantidad"])


  prod["cantidad"] -= unidades
  return prod["cantidad"]


  inv = {"A1":{"cantidad":3}, "B2":{"cantidad":0}}
  vender(inv, "A1", 2)
  vender(inv, "B2", 1)
  vender(inv, "C3", 1)
  vender(inv, "A1", -5)