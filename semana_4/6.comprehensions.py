# Ejercicio 1
precios = [120, 50, 200, 30, 400]
precios_sobre_100 = [c for c in precios if c > 100]
print(precios_sobre_100)
# Ejercicio 2
notas = {"Ana": 8, "Luis": 5, "Marta": 9, "Pedro": 6}
aprobados = {alumno:puntuacion for alumno,puntuacion in notas.items() if puntuacion > 6}
print(aprobados)
# Ejercicio 3
frase = "python es divertido y python es poderoso"
palabras_unicas = {palabra for palabra in frase.split()}
print(palabras_unicas)
# Ejercicio 4
productos = [("Pan", 20), ("Leche", 15), ("Carne", 80), ("Jugo", 10)]
orden_productos = {producto: ('caro' if precio > 30 else 'barato') for producto,precio in productos}
print(orden_productos)

# Ejercicio 5
usuarios = {f"user{i}": 1000 + i for i in range(1,6)}
print(usuarios)
# Ejercicio 6
nombres = ["Ana", "Luis", "Marta"]
letras = {letra.lower() for nombre in nombres for letra in nombre if letra.lower()}
print(letras)