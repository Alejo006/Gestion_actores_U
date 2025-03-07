from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, materia, creditos, codigo):
        super().__init__(nombre, edad, direccion)
        self.__materia = materia
        self.__creditos = creditos
        self.__codigo = codigo

    # Getters y Setters
    def getmateria(self):
        return self.__materia

    def setmateria(self, materia):
        self.__materia = materia

    def getcreditos(self):
        return self.__creditos

    def setcreditos(self, creditos):
        self.__creditos = creditos

    def getcodigo(self):
        return self.__codigo

    def setcodigo(self, codigo):
        self.__codigo = codigo

    # Método para actualizar datos del profesor
    def actualizar(self, nombre=None, edad=None, direccion=None, materia=None, creditos=None, codigo=None):
        super().actualizar(nombre, edad, direccion)  # Llama al método de Persona para actualizar nombre, edad y dirección
        if materia:
            self.__materia = materia
        if creditos is not None:
            self.__creditos = creditos
        if codigo:
            self.__codigo = codigo

    # Método para borrar datos del profesor
    def borrar(self):
        super().borrar()  # Borra los datos de Persona
        self.__materia = None
        self.__creditos = None
        self.__codigo = None

    # Método __str__ 
    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Materia: {self.getmateria()}\n"
                f"Créditos: {self.getcreditos()}\n"
                f"Código de la materia: {self.getcodigo()}")