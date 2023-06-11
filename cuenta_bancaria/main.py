from Cliente import Cliente

mi_cliente = Cliente()
print(mi_cliente.__str__())
opcion = 0

while opcion != 'S':
    print('\nElige: Depositar (D), Retirar (R) o Salir (S)')
    opcion = input().upper()
    if opcion == 'D':
        carga = input('Introduza la cantidad de efectivo que desea ingresas: \n')
        mi_cliente.depositar(carga)
    elif opcion == 'R':
        retirada = input('Introduzca la cantidad que desea retirar: \n')
        mi_cliente.retirar(retirada)
print('Gracias por operar desde nuestra sucursal')

