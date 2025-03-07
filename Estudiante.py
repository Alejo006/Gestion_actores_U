from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso, dia):
        super().__init__(nombre, edad, direccion)
        self.__curso = curso
        self.__dia = dia

    # Getters y Setters
    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    # Método para actualizar datos del estudiante
    def actualizar(self, nombre=None, edad=None, direccion=None, curso=None, dia=None):
        super().actualizar(nombre, edad, direccion)
        if curso:
            self.__curso = curso
        if dia:
            self.__dia = dia

    # Método para borrar datos del estudiante
    def borrar(self):
        super().borrar()
        self.__curso = None
        self.__dia = None

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.__curso}, Día: {self.__dia}"
