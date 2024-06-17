class SaldoEfectivoInsuficiente(Exception):
    pass

class SaldoCuentaInsuficiente(Exception):
    pass

class Cuenta:
    def __init__(self,numero_cuenta,nombre,saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.saldo = saldo

class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible = 100000
        self.cuentas ={}
        self.cuenta_actual = None
    
    def agregar_cuenta(self,cuenta):
        self.cuentas[cuenta.numero_cuenta] = cuenta

    def autenticar(self,numero_cuenta):
        if numero_cuenta in self.cuentas:
            self.cuenta_actual = self.cuentas[numero_cuenta]
            print(f"Autenticación exitosa. Bienvenido, {self.cuenta_actual.nombre}.")
        else:
            print("Número de cuenta no válido.")

    def mostrar_datos_cuenta(self):
        if self.cuenta_actual:
            print(f"Nombre: {self.cuenta_actual.nombre}")
            print(f"Saldo: ${self.cuenta_actual.saldo}") 
        else:
            print("No hay ninguna cuenta autenticada.")
        
    def deposito_propio(self,monto):
        if self.cuenta_actual:
            self.cuenta_actual.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.cuenta_actual.saldo}")
        else:
            print("No hay ninguna cuenta autenticada.")
    
    def deposito_terceros(self, numero_cuenta_destino, monto):
        if numero_cuenta_destino in self.cuentas:
            self.cuentas[numero_cuenta_destino].saldo += monto
            print(f"Depósito exitoso en la cuenta {numero_cuenta_destino}.")
        else:
            print("Número de cuenta destino no válido.")

    def transferencia(self, numero_cuenta_destino, monto):
        if self.cuenta_actual:
            if monto > self.cuenta_actual.saldo:
                raise SaldoCuentaInsuficiente("Saldo insuficiente en la cuenta para realizar la transferencia.")
            if numero_cuenta_destino in self.cuentas:
                self.cuenta_actual.saldo -= monto
                self.cuentas[numero_cuenta_destino].saldo += monto
                print(f"Transferencia exitosa. Nuevo saldo: ${self.cuenta_actual.saldo}")
            else:
                print("Número de cuenta destino no válido.")
        else:
            print("No hay ninguna cuenta autenticada.")

    def retiro_efectivo(self, monto):
        if self.cuenta_actual:
            if monto > self.cuenta_actual.saldo:
                raise SaldoCuentaInsuficiente("Saldo insuficiente en la cuenta para realizar el retiro.")
            if monto > self.efectivo_disponible:
                raise SaldoEfectivoInsuficiente("Saldo insuficiente en el cajero para realizar el retiro.")
            self.cuenta_actual.saldo -= monto
            self.efectivo_disponible -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.cuenta_actual.saldo}. Efectivo disponible en cajero: ${self.efectivo_disponible}")
        else:
            print("No hay ninguna cuenta autenticada.")

# Ejemplo de uso
cuenta1 = Cuenta("123456", "Emilio Gomez", 5000)
cuenta2 = Cuenta("654321", "Maria Gomez", 3000)

cajero = CajeroAutomatico()
cajero.agregar_cuenta(cuenta1)
cajero.agregar_cuenta(cuenta2)

cajero.autenticar("123456")
cajero.mostrar_datos_cuenta()
cajero.deposito_propio(2000)
cajero.transferencia("654321", 1000)
cajero.retiro_efectivo(3000)
cajero.mostrar_datos_cuenta()
