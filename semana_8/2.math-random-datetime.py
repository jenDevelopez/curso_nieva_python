# Ejercicio 1
import random
from datetime import date,datetime
import statistics, math

print(random.randint(1,6))

# Ejercicio 2
nombres = ['luis','silvia','maria','pedro']
print(random.sample(nombres, 2))

# Ejercicio 3

hoy = date.today()
navidad = date(2025,12,25)
print(navidad - hoy)

# Ejercicio 4
numeros = random.sample(range(1,10), k=5)
promedio = statistics.mean(numeros)
print(numeros)
print(promedio)
print(math.ceil(promedio))

# Ejercicio 5

tarea = input('escribe tu tarea ')
ahora = datetime.now()
print(ahora.strftime("%d/%m/%Y"), ahora.strftime("%H:%M:%S"), tarea)
