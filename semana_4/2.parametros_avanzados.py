#Ejercicio 1
def listar_personas(*nombres):
  for nombre in nombres:
    print(nombre)

listar_personas('sara','raul','pepe')

#Ejercicio 2
def calcular_promedio(*nums):
  return sum(nums)/len(nums)


notas = (1,2,3,4)
promedio = calcular_promedio(*notas) # Unpack the tuple using *
print(promedio)
# Ejercicio 3
def registrar_producto(id,**datos):
  producto = datos
  producto['id'] = id
  return producto


producto_nuevo = registrar_producto(1, nombre="Laptop", marca="Dell", precio=1200)
print(producto_nuevo)

# Ejercicio 4
def crear_reporte(*notas,**datos_extra):
  print("Notas:")
  for nota in notas:
    print(nota)

  print("\nDatos Extra:")
  for dato in datos_extra:
    print(dato)


crear_reporte('nota1','nota2','nota3',nota1='blablabla',nota2='blebleble')

# Ejercicio 5
def presentar(nombre,edad,ciudad):
  print(f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")


presentar('Jennifer',33 ,'Murcia')