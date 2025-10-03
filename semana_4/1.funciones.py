#Ejercicio 1
def bienvenida():
  print("¡Hola estudiante!")

bienvenida()

#Ejercicio 2
def presentacion(nombre):
  print(f"Hola {nombre}")

presentacion("Jennifer")

#Ejercicio 3
def multiplicar(a,b):
  return a * b

print(multiplicar(2,2))

#Ejercicio 4
def ejemplo_print(a, b):
    print(a + b)  # solo muestra, no se puede reutilizar

def ejemplo_return(a, b):
    return a + b  # devuelve el valor

ejemplo_print(2, 3)        # Muestra 5 en pantalla
resultado = ejemplo_return(2, 3)
print(resultado * 2)

#Ejercicio 5
curso = 'Python'
def definir_curso():
  curso = 'Java'
  return curso

print(curso)
print(definir_curso())
