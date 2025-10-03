#Ejercicio 1
nombres = []
nombres.append("Paula")
nombres.append("Max")
print(nombres)
nombres.insert(0,"Anastasia")
print(nombres)
#Ejercicio 2
numeros = [1,2]
numeros.extend([3,4,5])
print(numeros)
#Ejercicio 3
colores = ["rojo","verde","azul","verde"]
colores.remove("verde")
print(colores)
colores.pop()
print(colores)
#Ejercicio 4
letras = ["a","b","c","b","a","b"]
print(letras.index("b"))
print(f"La letra b sale {letras.count('b')} veces en la lista letras")
#Ejercicio 5
nums = [5,1,4,2,3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
#Ejercicio 6
decenas = [10,20,30]
print(decenas)
decenas.clear()
print(decenas)