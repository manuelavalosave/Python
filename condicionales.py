#Obtenemos la edad del usuario final
edad = int(input("Escribe tu edad: "))
#se realiza la condicion para validar el numero ingresado
if edad > 17:
    #si es verdadero entonce mostrara este mensaje
    print("Eres mayor de edad")
elif edad == 18:
    print("Ya puedes Votar ")
else:
    #sino se cumple se muestra este mensaje
    print("Eres menor de edad")

