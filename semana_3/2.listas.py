#Ejercicio 1
paises = ["España", "Francia", "Brasil","Ucrania"]
print(paises[0],paises[3])
#Ejercicio 2
numeros = [1,3,8,6,5]
print(numeros[-1],numeros[-2])
#Ejercicio 3
colores = ["rojo","verde","azul"]
colores[1] = "amarillo"
print(colores)
#Ejercicio 4
letras = ["a","b","c","d","e","f"]
print(letras[:3])
print(letras[-3:])
print(letras[2:4])
#Ejercicio 5
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
#Ejercicio 6
animales = ["perro","gato","pez","gato"]
print("gato" in animales)
#Ejercicio 7
nombres = ["Ana","Luis","Marta"]
for nombre in nombres:
  print(nombre)

#Ejercicio 8
a = [1,2,3]
b = a
b[0] = 100 #el valor de [0] se cambia tanto en a como en b
print(a,b)

#Ejercicio 9
lista = [1,2,2,3,2,4]
print(2 in lista)
count = 0
for num in lista:
  if num == 2:
    count+=1

print(f"El 2 sale {count} veces")
lista2 = [2,1,2,3,2,4]
print(lista == lista2)