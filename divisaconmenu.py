menu = """
Bienvenido al Conversor de monedas 💰💰

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opcion:
"""
opcion = input(menu)

if opcion == '1':
    # obtenemos la cantidad de la moneda que debemos convertir
    pesos = input("Cuantos pesos colombianos tienes?: ")
    # hacemos la conversion de tipo decimal
    pesos = float(pesos)
    #asignamos una constante del valor del dolar
    valor_dolar = 3875
    #realizamos la operacion de la convercion
    dolares = pesos / valor_dolar
    #mostramos solo dos decimales
    dolares = round(dolares, 2)
    #lo convertimos a caracteres
    dolares = str(dolares)
    #finalmete lo mostramos a nuestro usuario final
    print("Tienes $" + dolares + " dolares")
elif opcion == '2':
        # obtenemos la cantidad de la moneda que debemos convertir
    pesos = input("Cuantos pesos Argentinos tienes?: ")
    # hacemos la conversion de tipo decimal
    pesos = float(pesos)
    #asignamos una constante del valor del dolar
    valor_dolar = 65
    #realizamos la operacion de la convercion
    dolares = pesos / valor_dolar
    #mostramos solo dos decimales
    dolares = round(dolares, 2)
    #lo convertimos a caracteres
    dolares = str(dolares)
    #finalmete lo mostramos a nuestro usuario final
    print("Tienes $" + dolares + " dolares")
elif opcion == '3':
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
else:
    print("Ingresa una opcion correcta")