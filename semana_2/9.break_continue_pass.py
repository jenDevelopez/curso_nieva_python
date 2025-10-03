#Ejercicio 1
for i in range(11):
  print(i)
  if i == 6:
    break

print('-------------')
#Ejercicio 2
for i in range(6):
  if(i == 3):
    continue
  print(i)

print('-------------')

#Ejercicio 3
for i in range(5):
  if(i == 2):
    pass
  print(i)

print('-------------')
#Ejercicio 4
for i in range(11):
  if(i % 2 == 0):
    continue
  print(i)
  if(i == 7):
    break