#Ejercicio 1
usuario = {"nombre":"Luis","pais":"MX"}
print(usuario.get("edad",0))
#Ejercicio 2
producto = {"nombre":"Laptop","precio":15000,"stock":10}
print(producto.keys())
print(producto.values())
for key,value in producto.items():
  print(key,"->",value)
#Ejercicio 3
perfil = {"usuario":"mike","rol":"viewer"}
data = {"rol":"admin","activo":True}
perfil.update(data)
print(perfil)
#Ejercicio 4
cfg = {"tema":"oscuro","notificaciones":True}
print(cfg.pop("tema"))
print(cfg.pop("idioma","es"))
print(cfg)
#Ejercicio 5
d = {"a":1,"b":2,"c":3}
d.popitem()
print(d)
d.popitem()
print(d)
#Ejercicio 6
a = {"x":[1,2]}
b = a
b["x"].append(3)
c = a.copy()
c["x"].append(4)
print(a,b,c) #b apunta al mismo espacio en memoria que a, y c es una copia superficial, por lo que los cambios se hacen en todos los casos
#Ejercicio 7
temp = {"k1":1,"k2":2}
print(temp)
temp.clear()
print(temp)
#Ejercicio 8
campos = ["nombre","email","telefono"]
data = dict.fromkeys(campos,None)
print(data)
usr = {"nombre":"Maria","email":"ana@mail.com","telefono":1234}
data.update(usr)
print(data)
#Ejercicio 9
config = {"modo":"auto"}
act = {"modo":"manual","reintentos":3}
config.update(act)
print(config)
print(config.get("timeout",30))
print(config.pop("reintentos"))
print(config)
#Ejercicio 10
persona = {"nombre":"Ana","edad":25}
print(persona.get("altura","No registrada"))
for clave,valor in persona.items():
  print(clave,"->",valor)