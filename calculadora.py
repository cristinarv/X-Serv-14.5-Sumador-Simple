#!/usr/bin/python3
# Cristina del Río Vergel
# Segunda versión de la calculadora(hecha con funciones)

import sys

def suma(operando1, operando2):
    return operando1 + operando2

def resta(operando1, operando2):
    return operando1 - operando2

def multi(operando1, operando2):
    return operando1 * operando2

def div(operando1, operando2):
    try:
        return operando1 / operando2
    except ZeroDivisionError:
        return("Error, estas dividiendo entre cero")

def elev(operando1, operando2):
    return operando1**operando2

funciones = {  # Hago el diccionario
    "mas": suma,
    "menos": resta,
    "multiplicado": multi,
    "dividido": div,
    "elevado": elev
}

if __name__ == "__main__":  # Para poder importarlo
    NUM_ARGS = 4

    if len(sys.argv) != NUM_ARGS:  # Control de argumentos
        sys.exit("uso: python3 calculadora.py función operando1 operando2")
    _, funcion, op1, op2 = sys.argv  # Para poder guardar los argumentos

    try:
        num1 = float(operando1)
        num2 = float(operando2)
        resultado = funciones[operacion](num1, num2)
    except ValueError:
        sys.exit("Error, solo puedes meter operandos que sean numeros.")
    except KeyError:
        sys.exit("Error: mas, menos, multiplicado, dividido, elevado")
    print(str(resultado))
