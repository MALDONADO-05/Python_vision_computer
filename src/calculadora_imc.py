weight_txt = input("Peso(kg): ")
height_txt = input("Altura (m): ")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight / height**2
    print("Tu IMA es {imc}")

except  ValueError:
    print("Datos invalidos. Ej.: peso 70.5, altura 1.75")
except ZeroDivisionError:
    print("Dato invalido para la division, no permitido 0")
except Exception as err:
    print(err)
print(f"TU imc es {imc}")

