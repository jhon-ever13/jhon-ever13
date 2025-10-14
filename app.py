"""
Autor: Ever Nuñez
Descripción: Ejemplo simple de aplicación en Python.
Este programa pide un nombre y muestra un menú básico.
Fecha: 2025-10-14
"""

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Calcular cuadrado de un número")
    print("3. Salir")

def saludar(nombre):
    print(f"\n¡Hola, {nombre}! 😊 Qué gusto verte por aquí.")

def calcular_cuadrado():
    try:
        numero = float(input("\nIngresa un número: "))
        print(f"El cuadrado de {numero} es {numero ** 2}")
    except ValueError:
        print("⚠️ Error: Ingresa un valor numérico válido.")

if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ")
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            saludar(nombre)
        elif opcion == "2":
            calcular_cuadrado()
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida, intenta otra vez.")
