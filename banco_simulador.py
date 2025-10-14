"""
Autor: Ever Nuñez
Proyecto: Simulador de Banco en Python
Descripción:
Este programa simula un sistema bancario con múltiples operaciones:
- Consultar saldo
- Depositar
- Retirar
- Transferir entre cuentas
- Solicitar préstamo
- Invertir dinero
- Mostrar historial de operaciones

Fecha: 2025-10-14
"""

import time
import random

# ==============================================
# CLASES PRINCIPALES
# ==============================================
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historial = []

    def consultar_saldo(self):
        print(f"\n💰 Saldo actual de {self.titular}: S/ {self.saldo:.2f}")

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self._registrar(f"Depósito de S/ {monto:.2f}")
            print(f"✅ Se depositó correctamente S/ {monto:.2f}")
        else:
            print("⚠️ Monto inválido para depósito.")

    def retirar(self, monto):
        if monto <= 0:
            print("⚠️ El monto debe ser mayor que cero.")
            return
        if monto > self.saldo:
            print("❌ Fondos insuficientes.")
        else:
            self.saldo -= monto
            self._registrar(f"Retiro de S/ {monto:.2f}")
            print(f"💸 Se retiró S/ {monto:.2f} exitosamente.")

    def transferir(self, otra_cuenta, monto):
        if monto <= 0:
            print("⚠️ El monto debe ser mayor que cero.")
            return
        if monto > self.saldo:
            print("❌ Fondos insuficientes para transferir.")
        else:
            self.saldo -= monto
            otra_cuenta.saldo += monto
            self._registrar(f"Transferencia de S/ {monto:.2f} a {otra_cuenta.titular}")
            otra_cuenta._registrar(f"Transferencia recibida de S/ {monto:.2f} de {self.titular}")
            print(f"💳 Transferencia de S/ {monto:.2f} realizada con éxito a {otra_cuenta.titular}.")

    def solicitar_prestamo(self, monto):
        if monto <= 0:
            print("⚠️ Monto inválido.")
            return
        interes = monto * 0.1
        total_a_pagar = monto + interes
        self.saldo += monto
        self._registrar(f"Préstamo aprobado de S/ {monto:.2f}. Total a pagar: S/ {total_a_pagar:.2f}")
        print(f"🏦 Préstamo aprobado: S/ {monto:.2f}")
        print(f"💡 Deberás pagar S/ {total_a_pagar:.2f} en el futuro (incluye intereses).")

    def invertir(self, monto, tasa=0.05):
        if monto <= 0 or monto > self.saldo:
            print("⚠️ Monto inválido para inversión.")
            return
        print(f"\n💼 Invirtiendo S/ {monto:.2f} al {tasa*100}% anual...")
        self.saldo -= monto
        self._registrar(f"Inversión de S/ {monto:.2f} al {tasa*100}%")
        time.sleep(1)
        ganancia = monto * tasa
        self.saldo += monto + ganancia
        self._registrar(f"Ganancia de inversión: S/ {ganancia:.2f}")
        print(f"✅ Inversión completada. Ganaste S/ {ganancia:.2f}.")

    def mostrar_historial(self):
        print(f"\n📜 Historial de operaciones ({self.titular}):")
        if not self.historial:
            print("No hay operaciones registradas aún.")
        else:
            for i, evento in enumerate(self.historial, 1):
                print(f"{i}. {evento}")

    def _registrar(self, descripcion):
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")
        self.historial.append(f"[{fecha}] {descripcion}")


# ==============================================
# CLASE DEL BANCO
# ==============================================
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}

    def crear_cuenta(self, titular, saldo_inicial=0):
        if titular in self.cuentas:
            print("⚠️ Ya existe una cuenta con ese nombre.")
            return
        cuenta = CuentaBancaria(titular, saldo_inicial)
        self.cuentas[titular] = cuenta
        print(f"🏦 Cuenta creada para {titular} con saldo inicial S/ {saldo_inicial:.2f}")

    def obtener_cuenta(self, titular):
        return self.cuentas.get(titular)

    def listar_cuentas(self):
        print(f"\n🏦 Cuentas registradas en {self.nombre}:")
        if not self.cuentas:
            print("No hay cuentas registradas todavía.")
        for nombre, cuenta in self.cuentas.items():
            print(f"- {nombre} | Saldo: S/ {cuenta.saldo:.2f}")


# ==============================================
# FUNCIONES DE INTERFAZ
# ==============================================
def menu_principal():
    print("\n===== 🏦 BANCO NACIONAL PYTHON =====")
    print("1. Crear cuenta")
    print("2. Consultar saldo")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Transferir dinero")
    print("6. Solicitar préstamo")
    print("7. Invertir dinero")
    print("8. Ver historial")
    print("9. Ver todas las cuentas")
    print("0. Salir")

def pausar():
    input("\nPresiona ENTER para continuar...")


# ==============================================
# PROGRAMA PRINCIPAL
# ==============================================
def main():
    banco = Banco("Banco Nacional Python")
    while True:
        menu_principal()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del titular: ")
            saldo = float(input("Saldo inicial: "))
            banco.crear_cuenta(nombre, saldo)

        elif opcion == "2":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                cuenta.consultar_saldo()
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "3":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                monto = float(input("Monto a depositar: "))
                cuenta.depositar(monto)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "4":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                monto = float(input("Monto a retirar: "))
                cuenta.retirar(monto)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "5":
            origen = input("Cuenta origen: ")
            destino = input("Cuenta destino: ")
            monto = float(input("Monto a transferir: "))
            cuenta_origen = banco.obtener_cuenta(origen)
            cuenta_destino = banco.obtener_cuenta(destino)
            if cuenta_origen and cuenta_destino:
                cuenta_origen.transferir(cuenta_destino, monto)
            else:
                print("⚠️ Alguna de las cuentas no existe.")

        elif opcion == "6":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                monto = float(input("Monto del préstamo: "))
                cuenta.solicitar_prestamo(monto)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "7":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                monto = float(input("Monto a invertir: "))
                tasa = float(input("Tasa de interés (ej: 0.05 para 5%): "))
                cuenta.invertir(monto, tasa)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "8":
            nombre = input("Titular de la cuenta: ")
            cuenta = banco.obtener_cuenta(nombre)
            if cuenta:
                cuenta.mostrar_historial()
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "9":
            banco.listar_cuentas()

        elif opcion == "0":
            print("\n👋 Gracias por usar el simulador bancario. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

        pausar()


# ==============================================
# EJECUCIÓN
# ==============================================
if __name__ == "__main__":
    main()
