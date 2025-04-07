class DatoPolinomio (object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

    def __repr__(self):
        return f"DatoPolinomio(valor={self.valor}, termino={self.termino})"
    
    @staticmethod
    def crear_polinomio_grado_cero(valor):
        return DatoPolinomio(valor=valor, termino=0)
    
    def agregar_termino(self, valor, termino):
        self.valor += valor
        self.termino = max(self.termino, termino)
