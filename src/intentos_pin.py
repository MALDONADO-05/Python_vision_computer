"""Este programa va a pedir al usuario su pin de acceso, 
si el pin es correcto, entoces el programa debe decirle autenticacion exitosa, 
acceso concendido.

si el pin es incorrecto, entonces el programa debe decirle pin incorrecto y el numero de intentos que le quedan 

si el usuario supera el numero de intentos permitidos entoces el programa le va a decir numero de intentos

superados y cuenta bloqeueada """
PIN_CORRECTO = "2005"
INTENTOS_MAXIMOS = 3
intentos = 0

while intentos < INTENTOS_MAXIMOS:
    entrada = input("ingresa tu pin (4 digitos)")
    if entrada == PIN_CORRECTO:
        print("autenticacion exitosa")
        print("acceso concedido")
        break
    else:
        intentos += 1
        restantes = INTENTOS_MAXIMOS - intentos
        if restantes > 0:
            print(f"Pin incorrecto. Te quedan {restantes}")
        else: 
            print("PIN INCORRECTO , CUENTA BLOQUEDA")
