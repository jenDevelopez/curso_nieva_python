#Ejercicio 1
numero = int(input('Introduce un numero '))
print('Positivo' if numero > 0 else 'Negativo' )
#Ejercicio 2
edad = int(input('introduce tu edad '))
print('Mayor de edad' if edad >= 18 else 'Menor de edad')
#Ejercicio 3
numero = int(input('Introduce un numero '))
print('Par' if numero % 2 == 0 else 'Impar')
#Ejercicio 4
es_admin = False
print('Acceso permitido' if es_admin else 'Acceso denegado')
#Ejercicio 5
nota = int(input('Introduce tu nota para evaluar'))
print('Excelente' if nota >= 90 else 'Aprobado' if nota >= 60 else 'Reprobado')