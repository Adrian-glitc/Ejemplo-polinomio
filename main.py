class DatoPolinomio(object):
    class Termino(object):
        def __init__(self, valor, termino):
            self.valor = valor
            self.termino = termino
            self.siguiente = None

        def __repr__(self):
            return f"Termino(valor={self.valor}, termino={self.termino})"

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(self, valor, termino):
        nuevo_termino = Termino(valor, termino)
        if self.termino_mayor is None or termino > self.grado:
            nuevo_termino.siguiente = self.termino_mayor
            self.termino_mayor = nuevo_termino
            self.grado = termino
        else:
            actual = self.termino_mayor
            while actual.siguiente is not None and actual.siguiente.termino > termino:
                actual = actual.siguiente
            if actual.termino == termino:
                actual.valor += valor
            else:
                nuevo_termino.siguiente = actual.siguiente
                actual.siguiente = nuevo_termino

    def __repr__(self):
        terminos = []
        actual = self.termino_mayor
        while actual is not None:
            terminos.append(f"{actual.valor}x^{actual.termino}")
            actual = actual.siguiente
        return " + ".join(terminos) if terminos else "0"

    def modificar_termino(self, termino, nuevo_valor):
        actual = self.termino_mayor
        while actual is not None and actual.termino != termino:
            actual = actual.siguiente
        if actual is not None:
            actual.valor = nuevo_valor

    def obtener_valor(self, termino):
        actual = self.termino_mayor
        while actual is not None:
            if actual.termino == termino:
                return actual.valor
            actual = actual.siguiente
        return 0

    def eliminar_termino(self, termino):
        actual = self.termino_mayor
        anterior = None
        while actual is not None and actual.termino != termino:
            anterior = actual
            actual = actual.siguiente
        if actual is not None:
            if anterior is None:
                self.termino_mayor = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente