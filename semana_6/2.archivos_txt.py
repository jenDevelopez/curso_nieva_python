# Ejemplo 1
with open('notas.txt', 'w', encoding="utf-8") as f:
  f.write("Comprar pan\n")
  f.write("Estudiar Python\n")

with open('notas.txt', 'a', encoding="utf-8") as f:
  f.write("Hacer ejercicio\n")

with open('notas.txt', 'r', encoding="utf-8") as f:
  for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")

# Ejercicio 1
with open('hola.txt','w', encoding="utf-8") as f:
  f.write('Hola Python')

# Ejercicio 2
with open('frases.txt','w', encoding="utf-8") as f:
  f.write('Aprender Python\n')
  f.write('Aprender Java\n')
  f.write('Aprender JavaScript\n')

# Ejercicio 3
with open('frases.txt','r',encoding="utf-8") as f:
  print(f.read())

# Ejercicio 4
with open('frases.txt', 'r', encoding="utf-8") as f:
  for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")

# Ejercicio 5
tareas = ["Comprar leche", "Estudiar Python", "Hacer ejercicio"]
with open('tareas.txt','w',encoding="utf-8") as f:
  for tarea in tareas:
    f.write(f"{tarea}\n")

# Ejercicio 6
new_list = []
with open('tareas.txt','r',encoding="utf-8") as f:
  for i, line in enumerate(f, start=1):
    new_list.append(line[:-1])

  print(new_list)


# Ejercicio 7
with open('tareas.txt','a',encoding="utf-8") as f:
  f.write("Leer un libro\n")
  f.write("Meditar\n")



# Ejercicio 8
with open('tareas.txt','r',encoding="utf-8") as f:
  total_lines = 0
  for i, linea in enumerate(f, start=1):
    total_lines += 1
  print(f"El numero total de lineas es {total_lines}")

# Ejercicio 9
with open('tareas.txt','r',encoding="utf-8") as origin:
  content = origin.read()
with open('tareas_backup.txt','w',encoding="utf-8") as destiny:
  destiny.write(content)

# Ejercicio 10
def guardar_notas(notas):
  with open('notas.txt','w', encoding="utf-8") as f:
    for nota in notas:
      f.write(f"{nota}\n")
  with open('notas.txt','r',encoding="utf-8") as f:
    for i,line in enumerate(f,start=1):
      print(f"{i}. {line.strip()}")


guardar_notas(['Escuchar kpop','programar','programar mientras escucho kpop'])