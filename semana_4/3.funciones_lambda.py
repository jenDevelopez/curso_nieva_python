# Ejercicio 1
suma = lambda x,y: x + y

print(suma(1,2))

# Ejercicio 2
esPar = lambda n: "par" if n%2== 0 else "impar"
print(esPar(2))
print(esPar(3))

# Ejercicio 3
cuadrado = lambda n: n**2
print(cuadrado(2))

# Ejercicio 4
str_reverse = lambda frase: frase[::-1]
print(str_reverse('hola'))

# Ejercicio 5
esMayor = lambda x,y: x if x > y else y
print(esMayor(1,2))

#Ejercicio 6
len_str = lambda str: len(str)
print(len_str('hola'))

# Ejercicio 7
saludo_lamda = lambda: print("Hola desde lambda")
saludo_lamda()

# Ejercicio 8
precioConIva = lambda precio: precio + (precio * 0.16)
print(precioConIva(100))

# Ejecicio 9
last_char = lambda s: s[-1]
last_char('hola')

# Ejercicio 10
operaciones_lambda = {
    'suma': lambda x, y: x + y,
    'resta': lambda x, y: x - y,
    'multiplicacion': lambda x, y: x * y,
    'division': lambda x, y: x / y

}