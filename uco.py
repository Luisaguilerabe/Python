def tabla(contador,tabla_2):
    contador = 1
    tabla_2 = 2 * contador
    while contador <= 10:
        print('2 por ' + str(contador) + ' es igual a: ' + str(tabla_2))
        contador += 1
        tabla_2 = 2 * contador

def run():
    menu = """
Bienvenido al conversor de monedas 💲💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """



opcion = int(input(menu))



if opcion == 1:
    tabla("Colombianos" , 3875)
elif opcion == 2:
    tabla("Argentinos" , 65)
elif opcion == 3:
    tabla("Mexicanos" , 24)
else:
    print('Ingresa una opcion correcta')



if __name__ == '__main__':
    run()