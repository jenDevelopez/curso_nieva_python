#Ejercicio 1
for letra in 'Python':
  print(letra)

print('---------------')
#Ejercicio 2
x = 5
while x >= 1:
  print(x)
  x -= 1

print('---------------')
#Ejercicio 3
numVocals = 0
for letra in 'programa':
  if letra in 'aeiou':
    numVocals += 1

print(numVocals)

print('---------------')
#Ejercicio 4
resultado = 0
x = 1
while x <= 3:
  resultado += x
  x += 1

print(resultado)
print('---------------')
#Ejercicio 5
password = ""
while password != 'python':
  password = input('introduce tu contraseña ')