from clases import Inicio, Partida
from time import sleep

                                        ## SIMON DICE ##

                                    ## ** MENU DE INICIO ** ##
inicio_juego = Inicio()
partida = Partida(inicio_juego.nombre,inicio_juego.reintentos)
partida.__str__()
opcion = input().upper()
                                    ## ** INSTRUCCIONES ** ##
while opcion != 'E':
    partida.instrucciones()
    sleep(4)
    partida.cuenta_atras('3')
    sleep(1)
    partida.cuenta_atras('2')
    sleep(1)
    partida.cuenta_atras('1')
    sleep(1)
    partida.ya()
    break
                                     ## ** PARTIDA ** ##


  #  opcion = input().upper()
# if opcion == 'A':
