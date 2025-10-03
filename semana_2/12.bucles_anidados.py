#Ejercicio 1
for i in range(3):
  for j in range(2):
    print(f"i = {i}, j = {j}")
print('------------')
#Ejercicio 2
x=""
for i in range(4):
  for j in range(4):
    x += '#'
  print(x)
  x = ''
print('-----------')
#Ejercicio 3
for letra in 'ab':
  for i in range(13):
    print(letra,i)
print('--------------')
#Ejercicio 4
for i in range(1,4):
  for j in range(4):
    print(f"{i} x {j} = {i*j}")