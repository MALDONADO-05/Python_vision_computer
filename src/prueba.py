name = "Hola mundo"
print(name)
#Built-in method input(argument)
user_name = input("como te llamas")
edad_txt = input("cual es tu edad")

#Built-in method input(argument)
print(user_name)
print(edad_txt)

print(edad_txt)
print(type(edad_txt))

#Meotodo buit-in int(1-argument) -convierte un string a un numero entero
try:
    edad = int(edad_txt)
    print(edad)
    print(type(edad))
except ValueError:
    print("Error: la conversion no se puede hacer") 
    print("Debes ingresar un numero entero")
    print("Fin del programa")   
 
