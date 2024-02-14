# Función para sumar 
def sumar(a, b):
    return a + b

# Función para restar 
def restar(a, b):
    return a - b

# Función para multiplicar 
def multiplicar(a, b):
    return a * b

# Función para dividir 
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero."

# Pedir al usuario que elija una opción
print("Seleccione una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = int(input("Ingrese el número de la opción deseada: "))

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada e imprimir consola
if opcion == 1:
    print("La suma es:", sumar(num1, num2))
elif opcion == 2:
    print("La resta es:", restar(num1, num2))
elif opcion == 3:
    print("La multiplicación es:", multiplicar(num1, num2))
elif opcion == 4:
    print("La división es:", dividir(num1, num2))
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")