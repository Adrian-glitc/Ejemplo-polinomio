from Polinomio import DatoPolinomio
from Operaciones import modificar_termino
from Operaciones import obtener_valor

def main():
    # Crear instancias de DatoPolinomio
    polinomio1 = DatoPolinomio()
    polinomio2 = DatoPolinomio()

    # Agregar términos a los polinomios
    polinomio1.agregar_termino(3, 2)  # 3x^2
    polinomio1.agregar_termino(5, 1)  # 5x^1
    polinomio1.agregar_termino(-2, 0) # -2

    polinomio2.agregar_termino(4, 1)  # 4x^1
    polinomio2.agregar_termino(1, 0)  # 1

    # Imprimir representación de los polinomios
    print("Polinomio 1:", polinomio1)  # Resultado: 3x^2 + 5x^1 - 2
    print("Polinomio 2:", polinomio2)  # Resultado: 4x^1 + 1

    # Modificar un término
    polinomio1.modificar_termino(1, 7)  # Cambiar 5x^1 a 7x^1
    print("Polinomio 1 después de modificar:", polinomio1)  # Resultado: 3x^2 + 7x^1 - 2

    # Obtener el valor de un término
    valor = polinomio1.obtener_valor(2)  # Obtener coeficiente de x^2
    print("Coeficiente de x^2 en Polinomio 1:", valor)  # Resultado: 3

    # Eliminar un término
    polinomio1.eliminar_termino(0)  # Eliminar término independiente (-2)
    print("Polinomio 1 después de eliminar término independiente:", polinomio1)  # Resultado: 3x^2 + 7x^1

    # Sumar dos polinomios
    suma = polinomio1.sumar(polinomio2)
    print("Suma de Polinomio 1 y Polinomio 2:", suma)  # Resultado: 3x^2 + 11x^1 + 1

    # Multiplicar dos polinomios
    producto = polinomio1.multiplicar(polinomio2)
    print("Producto de Polinomio 1 y Polinomio 2:", producto)  # Resultado: 12x^3 + 29x^2 + 7x^1
