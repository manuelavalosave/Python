# obtenemos la cantidad de la moneda que debemos convertir
pesos = input("Cuantos pesos Mexicanos tienes?: ")
# hacemos la conversion de tipo decimal
pesos = float(pesos)
#asignamos una constante del valor del dolar
valor_dolar = 22
#realizamos la operacion de la convercion
dolares = pesos * valor_dolar
#mostramos solo dos decimales
dolares = round(dolares, 2)
#lo convertimos a caracteres
dolares = str(dolares)
#finalmete lo mostramos a nuestro usuario final
print("Tienes $" + dolares + " dolares")