class TarjetaCredito:
    def __init__(self, tipo, limite_credito, limite_transaccion, limite_comida, tasa_interes, regla_puntos):
        self.tipo = tipo
        self.limite_credito = limite_credito
        self.limite_transaccion = limite_transaccion
        self.limite_comida = limite_comida
        self.saldo = 0
        self.tasa_interes = tasa_interes
        self.regla_puntos = regla_puntos
        self.puntos = 0
    
    def realizar_compra(self, monto, categoria="general"):
        limite_actual = self.limite_comida if categoria == "comida" else self.limite_transaccion
        
        if self.saldo + monto > self.limite_credito:
            print("Transacción rechazada: Límite de crédito general excedido.")
            return
        if monto > limite_actual:
            print(f"Transacción rechazada: No puede superar el límite de {limite_actual} por transacción.")
            return
        
        self.saldo += monto
        self.limite_credito -= monto
        self.acumular_puntos(monto, categoria)
        print(f"Compra de ${monto} realizada con éxito. Saldo actual: ${self.saldo}")
    
    def acumular_puntos(self, monto, categoria):
        factor = self.regla_puntos.get(categoria, self.regla_puntos["general"])
        self.puntos += monto // factor
    
    def generar_intereses(self):
        if self.saldo > 0:
            interes = self.saldo * self.tasa_interes
            self.saldo += interes
            print(f"Intereses de ${interes} aplicados. Nuevo saldo: ${self.saldo}")
    
    def realizar_pago(self, monto):
        if monto > self.saldo:
            monto = self.saldo
        if monto > self.limite_transaccion:
            print(f"Pago rechazado: No puede superar el límite de {self.limite_transaccion} por pago.")
            return
        
        self.saldo -= monto
        self.limite_credito += monto
        print(f"Pago de ${monto} realizado. Saldo restante: ${self.saldo}")
    
    def consultar_credito(self):
        print(f"Crédito disponible: ${self.limite_credito}")
    
    def consultar_puntos(self):
        print(f"Puntos acumulados: {self.puntos}")


def menu():
    tarjetas = {
        "Estandar": TarjetaCredito("Estandar", 1000000, 200000, 200000, 0.03, {"general": 2500}),
        "Premium": TarjetaCredito("Premium", 2000000, 500000, 500000, 0.015, {"general": 1000}),
        "Restaurante": TarjetaCredito("Restaurante", 1000000, 200000, 500000, 0.02, {"general": 2500, "comida": 1000})
    }
    
    while True:
        print("\n--- Sistema de Tarjetas de Crédito ---")
        tarjeta_tipo = input("Ingrese el tipo de tarjeta (Estandar, Premium, Restaurante) o 'salir' para salir: ")
        if tarjeta_tipo.lower() == "salir":
            print("Saliendo del sistema...")
            break
        
        tarjeta = tarjetas.get(tarjeta_tipo)
        if not tarjeta:
            print("Tipo de tarjeta inválido.")
            continue
        
        while True:
            print("\n--- Menú de acciones ---")
            print("1. Realizar Compra")
            print("2. Realizar Pago")
            print("3. Generar Intereses")
            print("4. Consultar Crédito Disponible")
            print("5. Consultar Puntos Acumulados")
            print("6. Cambiar tipo de tarjeta")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "6":
                break
            
            if opcion == "1":
                monto = float(input("Ingrese el monto de la compra: "))
                categoria = input("Ingrese la categoría (general/comida): ")
                tarjeta.realizar_compra(monto, categoria)
            elif opcion == "2":
                monto = float(input("Ingrese el monto del pago: "))
                tarjeta.realizar_pago(monto)
            elif opcion == "3":
                tarjeta.generar_intereses()
            elif opcion == "4":
                tarjeta.consultar_credito()
            elif opcion == "5":
                tarjeta.consultar_puntos()
            else:
                print("Opción inválida.")

menu()
