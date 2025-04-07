
from Polinomio import DatoPolinomio
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