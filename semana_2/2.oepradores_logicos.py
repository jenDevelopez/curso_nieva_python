# Ejercicio 1
numero = int(input('Introduce un numero '))
print('Tu numero esta entre 10 y 20' if numero >= 10 and numero <= 20 else 'Tu numero no esta entre 10 y 20')
# Ejercicio 2
notaAlumno = 50
tieneProyectoEspecial = True
print( 'Has aprobado' if notaAlumno > 60 or tieneProyectoEspecial == True else 'No has aprobado')
# Ejercicio 3
numero = 5
esPositivo = numero >= 0
print(not esPositivo)
# Ejercicio 4
edad = 15
tienePermiso = True
print(edad >= 18 and tienePermiso == True)
# Ejercicio
tieneBoleto = True
listaVip = False
edad = 15
print('Puede pasar ' if (edad >= 12) and (tieneBoleto == True or listaVip == True) else 'No puede pasar')
