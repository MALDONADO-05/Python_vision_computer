print("Este programa captura importes")
info = """

     Calcula tu suma

     Este programa lleva el conteo de importes va acumulado un usuario, va acumulado todos los importes que el usuario ingresa
     Si el usuario desea terminar el programa puede escribirse cualquier momento la palabra exit, quit, terminar

     """
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None
while True:
        user_message = ["""
    
                    Si quieres dejar de capturar importes puedes ingresar en cualquier momento exit,quit, terminar """]
    
        line = input(user_message).lower()
        if line =="exit" or line == "quit" or line == "terminar":
             break
        

try:
    value = float(line)
except ValueError:
    print("valor invalido, intente de nuevo ")
conteo += 1 #me dice cuantos numeros he ingresado
suma += value #me lleva la acumulacion

if minimo is None or value < minimo:
     minimo = value 
      
if maximo is None or value > maximo:
          maximo = value
if conteo == 0:
     print("no se capturaron importes")
else:
     print("="*32)
     print("La cantidad de numeros ingresados en: ",f"{conteo}")
     print("La sumatoria de todos los numeros es: ",f"{suma}")
     print("El minimo es:", f"{minimo}")
     print("El maximo es:", f"{maximo}")

print("programa finalizado")