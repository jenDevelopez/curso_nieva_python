#Ejercicio 1
alumno = {
    "nombre":"alex",
    "edad":25,
    "carrera":"arquitecto"
}
print(alumno["carrera"])
#Ejercicio 2
producto = {
    "nombre":"laptop",
    "precio":15000
}
producto["precio"] = 14000
producto["stock"] = 20
print(producto)
#Ejercicio 3
ciudad = {"nombre":"Veracruz","poblacion":600000,"pais":"México"}
del ciudad["pais"]
print(ciudad)
#Ejercicio 4
persona = {"nombre":"Luis","edad":30}
print("Edad encontrada" if "edad" in persona else "No existe")
#Ejercicio 5
contacto = {"nombre":"Ana","telefono":"1234","email":"ana@mail.com"}
for clave in contacto:
  valor = contacto[clave]
  print(clave,"->",valor)
#Ejercicio 6
a = {"x":1}
b = a
b["x"] = 2 #ambas variables apuntan al mismo espacio en memoria, asique cuando se muta el diccionario desde una de las variables, cambian ambas
print(a,b)
print(a,b)

#Ejercicio 7
c = a.copy()
c["x"] = 5 #con la variable c se ha hecho una copia superficial, apuntan a distintos espacion de memoria, por lo tanto cuando se muta c["x"] no afecta a a["x"]
print(a,c)

#Ejercicio 8
datos = {"nums":[1,2,3]}
copia = datos.copy()
print(datos,copia)
copia["nums"].append(4)
print(datos,copia) #se hace una copia superficial, y se accede al mismo espacio en memoria
#Ejercicio 9
usuario = {
    "nombre": "Maximo",
    "edad":37,
    "contacto":{"email":"max@gmail.com","telefono":123456789}
}
print(usuario["contacto"]["email"])
#Ejercicio 10
agenda = {
    "Alicia":{"telefono":12346789,"email":"ali@gmail.com"},
    "Luis": {"telefono":12346789,"email":"luis@gmail.com"},
    "Pepe": {"telefono":12346789,"email":"pepe@gmail.com"}
}

for nombre in agenda:
  data = agenda[nombre]
  print(nombre, "->", data)