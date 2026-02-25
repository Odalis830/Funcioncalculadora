print(" Mi Super Calculadora ")

num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

if operacion == "+":
    resultado = num_1 + num_2
    print("Resultado:", resultado)

if operacion == "-":
    resultado = num_1 - num_2
    print("Resultado:", resultado)

if operacion == "*":
    resultado = num_1 * num_2
    print("Resultado:", resultado)

if operacion == "/":
    if num_2 != 0:
        resultado = num_1 / num_2
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre 0
