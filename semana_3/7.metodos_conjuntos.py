from re import X
#Ejercicio 1
frutas = {"manzana","pera"}
frutas.add("uva")
print(frutas)
#Ejercicio 2
colores = {"rojo", "verde", "azul"}
colores.remove("verde")
print(colores)
colores.discard("negro")
print(colores)
#Ejercicio 3
letras = {"a","b","c","d"}
print(letras.pop())
print(letras)
#Ejercicio 4
nums = {1,2,3}
nums.clear()
print(nums)
#Ejercicio 5
a = {1,2,3}
b = {3,4,5}
a.update(b)
print(a)
#Ejercicio 6
a = {1,2,3,4}
b = {3,4,5}
a.intersection_update(b)
print(a)
#Ejercicio 7
a = {1,2,3,4}
a.difference_update({2,5})
print(a)
#Ejercicio 8
a = {1,2,3}
b = {3,4}
a.symmetric_difference_update(b)
print(a)
#Ejercicio 9
x = {1,2}
y = {2,3,4}
z = x.union(y)
print(z)
print(x | y)
#Ejercicio 10
xy = x.intersection(y)
print(xy)
print(x & y)
#Ejercicio 11
d1 = x - y
d2 = y - x
print(f"d1 -> {d1}")
print(f"d2 -> {d2}")
#Ejercicio 12
sd = x.symmetric_difference(y)
print(sd)
print(x ^ y)
#Ejercicio 13
a = {1,2}
b = {1,2,3,4}
print(a.issubset(b)) #a es un subconjunto de b, lo que quiere decir que el contenido de a se encuentra en b
print(b.issuperset(a)) #b es un superconjunto de a, lo que quiere decir que el contenido de a forma parte de b
#Ejercicio 14
m = {"py","js"}
n = {"html","css"}
print(m.isdisjoint(n))
p = {"js","go"}
print(m.isdisjoint(p)) #Da False porque ambos sets comparten el valor "js"