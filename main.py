class DatoPolinomio(object):
    def __init__(self):
        self.terminos = {}
        self.grado = -1

    def agregar_termino(self, valor, termino):
        if termino in self.terminos:
            self.terminos[termino] += valor
        else:
            self.terminos[termino] = valor
        if termino > self.grado:
            self.grado = termino

    def __repr__(self):
        terminos = [f"{valor}x^{termino}" for termino, valor in sorted(self.terminos.items(), reverse=True) if valor != 0]
        return " + ".join(terminos) if terminos else "0"

    def modificar_termino(self, termino, nuevo_valor):
        if termino in self.terminos:
            self.terminos[termino] = nuevo_valor

    def obtener_valor(self, termino):
        return self.terminos.get(termino, 0)

    def eliminar_termino(self, termino):
        if termino in self.terminos:
            del self.terminos[termino]
        if termino == self.grado:
            self.grado = max(self.terminos.keys(), default=-1)

    def mostrar(self):
        print(self.__repr__())

    def sumar(self, otro):
        resultado = DatoPolinomio()
        for termino, valor in self.terminos.items():
            resultado.agregar_termino(valor, termino)
        for termino, valor in otro.terminos.items():
            resultado.agregar_termino(valor, termino)
        return resultado

    def multiplicar(self, otro):
        resultado = DatoPolinomio()
        for termino1, valor1 in self.terminos.items():
            for termino2, valor2 in otro.terminos.items():
                nuevo_termino = termino1 + termino2
                nuevo_valor = valor1 * valor2
                resultado.agregar_termino(nuevo_valor, nuevo_termino)
        return resultado
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

if __name__ == "__main__":
    main()