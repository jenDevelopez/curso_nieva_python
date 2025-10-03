#Ejercicio 1
animales = ["perro","gato","pajaro","leon","pantera"]
print(len(animales))
#Ejercicio 2
numeros = [1,2,3,4,5,6,7,8,9,10]
print(sum(numeros))
#Ejercicio 3
t = (5, 17, 3, 9, 21)
print(f"El numero menor es {min(t)} y el numero mayor es {max(t)}")
#Ejercicio 4
puntos = [40, 10, 70, 20]
puntos_sort = sorted(puntos)
print(puntos_sort)
puntos_rev = list(reversed(puntos_sort))
print(puntos_rev)
#Ejercicio 5
lng = "python"
print(list(reversed(lng)))
#Ejercicio 6
valores = {0, "", None, 15}
print(any(valores))
#Ejercicio 7
checks = {"a": 1, "b": True, "c": "ok"}
print(all(checks.values())) #Devuelve True porque todos los  valores son verdaderos