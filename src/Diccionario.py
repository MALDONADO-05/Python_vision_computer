#datos del diccionario
info_charly = {"name": 'charly', "age": 33, "adress" : "18 O.R", "salary": 100, "married": True}
#imprimir especifico datos del diccionario
print(info_charly['name'])

print(info_charly.keys())

print(info_charly.values())
#para imprimir todos los datos del diccionario
for key,value in info_charly.items():
    print(key,value)

print(info_charly.get("gender",""))