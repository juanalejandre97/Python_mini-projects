from Python_mini-projects.cuenta_bancaria.Persona import Persona


class Cliente(Persona):
    def __init__(self):
        print('\n¡Bienvenido a nuestra oficina! Ingrese por favor los siguientes datos:')
        self.nombre = input('Nombre:\n')
        self.apellido = input('Apellido:\n')
        self.nif = input('NIF:\n')
        self.numero_cuenta = input('Nº de cuenta:\n')
        self.balance = 0
    def __str__(self):
        print(f'Cliente: {self.nombre} {self.apellido}. Número de cuenta: '
              f'{self.numero_cuenta} \nBalance de {self.balance} € en la cuenta')
    def isfloat(self,input):
        try:
            input = float(input)
            return True
        except:
            print('Introduzca un importe numérico, por favor:')
        return False

    def ispositiv(self,input):
        if float(input) < 0:
            print('Introduzca un importe positivo, por favor:')
            return False
        else:
            return True
    def sup(self,input):
        if float(input) > self.balance:
            print('Su importe de retirada excede a su saldo disponible. Introduzca por favor \n'
                  'un importe de crédito válido:')
            return False
        else:
            return True

    def comprobante_retirada(self,retirada):
        while True:
            if self.isfloat(retirada) and self.ispositiv(retirada) and self.sup(retirada):
                break
            else:
                retirada = input('')
        print(f'El valor introducido es correcto y su saldo ahora es {self.balance - float(retirada)} €')
        return retirada
    def comprobante_deposito(self,carga):
        flag = True
        while flag is True:
            if self.isfloat(carga) and self.ispositiv(carga):
                flag = False
            else:
                carga = input('')
        print(f'El valor introducido es correcto y su saldo ahora es {float(self.balance) + float(carga)} €')
        return carga
    def depositar(self,carga):
        aux = self.comprobante_deposito(carga)
        self.balance += float(aux)
    def retirar(self,retirada):
        aux1 = self.comprobante_retirada(retirada)
        self.balance -= float(aux1)