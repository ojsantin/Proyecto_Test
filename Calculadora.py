def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    return x / y

def calculadora():
    print("Bienvenido a la Calculadora en Python")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        try:
            opcion = int(input("Seleccione una operación (1/2/3/4): "))
            if opcion not in [1, 2, 3, 4]:
                print("Opción no válida. Intente de nuevo.")
                continue

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = sumar(num1, num2)
                operacion = "+"
            elif opcion == 2:
                resultado = restar(num1, num2)
                operacion = "-"
            elif opcion == 3:
                resultado = multiplicar(num1, num2)
                operacion = "*"
            elif opcion == 4:
                resultado = dividir(num1, num2)
                operacion = "/"

            print(f"\nResultado: {num1} {operacion} {num2} = {resultado}\n")

            continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
            if continuar != "s":
                print("Gracias por usar la calculadora.")
                break

        except ValueError:
            print("Entrada inválida. Por favor ingrese números válidos.")

if __name__ == "__main__":
    calculadora()