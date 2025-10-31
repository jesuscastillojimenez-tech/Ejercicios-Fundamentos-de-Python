
class Calculadora:
    numero1 = 0
    numero2 = 0
    numero3 = 0

    def __init__(self, numero1=0, numero2=0, numero3=0):
        self._numero1 = numero1
        self._numero2 = numero2
        self._numero3 = numero3
        self._historial = []

    """----------setter and getter----------"""

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")

    @property
    def numero3(self):
        return self._numero3

    @numero3.setter
    def numero3(self, nuevo_numero3):
        if type(nuevo_numero3) in (int, float):
            self._numero3 = nuevo_numero3
        else:
            raise ValueError("Debe ser un número")

    # Métodos de operaciones
    def sumar(self):
        return self._numero1 + self._numero2

    def restar(self):
        return self._numero1 - self._numero2

    def multiplicar(self):
        return self._numero1 * self._numero2

    def dividir(self):
        if self._numero2 != 0:
            return self._numero1 / self._numero2
        else:
            return "Error: No se puede dividir entre cero."

    def potencia(self):
        try:
            return self._numero1 ** self._numero2
        except Exception as e:
            return f"Error potencia: {e}"

    def ver_historial(self):
        for operacion in self._historial:
            print(operacion)

    def agregar_a_historial(self, operacion):
        self._historial.append(operacion)
