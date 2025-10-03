from functools import reduce
# Ejercicio 1
celsius = [0, 10, 20, 30, 40]
to_farenheit =  list(map(lambda c: c*9/5 +32,celsius))

print(to_farenheit)

# Ejercicio 2
nombres = ['Maria','Juan','Jose']
saludos = list(map(lambda nombre: f"Hola {nombre}",nombres))
print(saludos)
# Ejercicio 3
edades = [5,10,85,2,69,25]
mayor_edad = list(filter(lambda edad: edad >= 18, edades))
print(mayor_edad)
# Ejercicio 4
lista_frases = ['hola caracola', 'ey','echa el freno macareno']
frases_largas = list(filter(lambda str: len(str) > 10, lista_frases))
print(frases_largas)
# Ejercicio 5
lista_precios = [8.50,1.25,6.00]
total_precios = reduce(lambda a,b: a+b,lista_precios)
print(total_precios)
# Ejercicio 6
lista_numeros = [5,8,25,47,658]
numero_mayor = reduce(lambda x,y: x if x > y else y,lista_numeros)
print(numero_mayor)
# Ejercicio 7
lista_palabras = ['CARACOLA','PERRO','MAR','PUERTA']
frases_start_p = list(map(lambda str: str.lower(),filter(lambda str: str[0] == 'P',lista_palabras)))
print(frases_start_p)
# Ejercicio 8
lista_precios_usd = [10,50,100]
lista_precios_mxn = list(map(lambda p: p * 17.5,lista_precios_usd))
total_precios_mxn = reduce(lambda x,y: x+y,lista_precios_mxn)
print(lista_precios_mxn)
print(total_precios_mxn)
# Ejercicio 9
promedio_edades_mayores = reduce(lambda x,y: x + y, mayor_edad) / len(mayor_edad)
print(promedio_edades_mayores)
# Ejercicio 10
lista_numeros = [1,8,6,10,25]
lista_pares = list(filter(lambda num:num % 2 == 0,lista_numeros))
total_pares = reduce(lambda x,y:x + y,lista_pares)
print(lista_pares)
print(total_pares)
