# Ejercicio 1
def presentar():
  return "Hola, soy estudiante"

f = presentar
f()
# Ejercicio 2
def aplicar_dos_veces(func,valor):
   for _ in range(2):
      return func(valor)

aplicar_dos_veces(str.upper,'python')
aplicar_dos_veces(len,'python')
# Ejercicio 3
def crear_sumador(n):
  def sumar(x):
    return x + n
  return sumar

sumar2 = crear_sumador(2)
print(sumar2(5))
