names = []

#metodo append para agregar elementos al final de la lista
names.append("angel")
names.append("charly")
names.append("alexis")
names.append("Erick")
names.append("Jona")
names.append("Arce")


print(names)
print(type(names))
print(len(names))

#metodo para agregar elementos en una posicion deseada
names.insert(1, "hector") #indice y luego elemento

print(names)

#metodo pop() sin indice para eliminar el ultimo elemento de la lista
names.pop()
print(names)

#Metodo pop() con indice para elimnar un elemento deseado con la posicion indice
names.pop(2)
print(names)

#Metodo remover(Val) para elimnar elementoss por valor 
names.pop("Jona")
print(names)
