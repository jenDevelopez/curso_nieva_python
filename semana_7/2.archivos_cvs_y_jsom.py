import csv
import json
# Se crea el archivo y se escriben los nombres

with open('nombres.csv','w',newline="", encoding="utf-8") as f:
  escritor = csv.writer(f)
  escritor.writerow(["nombre"])
  escritor.writerow(["Ana"])
  escritor.writerow(["Luis"])
  escritor.writerow(["Marta"])

# Se lee el archivo y se imprimen los nombres
with open('nombres.csv','r',encoding="utf-8") as f:
  lector = csv.reader(f)
  for fila in lector:
    print(fila)


# Ejercicio 2
with open('alumnos.csv','w',newline="",encoding="utf-8") as f:
  w = csv.writer(f)
  w.writerow(["Ana",33])
  w.writerow(["Luis",48])
  w.writerow(["Marta",20])

with open('alumnos.csv','r',encoding="utf-8") as f:
  r = csv.reader(f)
  for row in r:
    print(row)
    
    
# Ejercicio 3
user = {"name":"Jennifer","age":33}
with open('usuario.json','w',encoding="utf-8") as f:
  json.dump(user,f,ensure_ascii=False,indent=2)

with open('usuario.json','r',encoding="utf-8") as f:
  data = json.load(f)
  print(data)
  print(f"Hola {data['name']}, tienes {data['age']} años")
  
  
# Ejercicio 4
todos = [{"title":"hacer la cama","done":False},
    {"title":"ejercicios de python","done":False},
    {"title":"hacer la comida","done":True},
    {"title":"lavarse los dientes","done":True}]
with open('tareas.json','w',encoding="utf-8") as f:
  json.dump(todos,f,ensure_ascii=False,indent=2)

with open('tareas.json','r',encoding="utf-8") as f:
  data = json.load(f)
  for i in data:
    if(i['done'] == False):
      print(i)
      

# Ejercicio 5
with open('tareas.json','r',encoding="utf-8") as f:
  todos = json.load(f)
with open('tareas.csv','w',newline="",encoding="utf-8") as f:
  campos = ["title","done"]
  w = csv.DictWriter(f, fieldnames=campos)
  w.writeheader()
  w.writerows(todos)

with open("tareas.csv", "r", encoding="utf-8") as f:
  print(f.read())
  