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