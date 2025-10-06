# Ejemplo 1

#pip install requests

import requests
respuesta = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(respuesta.json())

# Ejemplo 2
#pip install numpy==1.26.4

import numpy as np
print("Versión instalada:", np.__version__)

# Ejemplo 3
# instalar libreria faker para generar usuario y contraseña falsos

#pip install faker

from faker import Faker
fake = Faker()

print("Usuario:", fake.user_name())
print("Contraseña", fake.password())