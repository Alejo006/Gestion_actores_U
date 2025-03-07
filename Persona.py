class Persona:
    def __init__(self, nombre, edad, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # Método para actualizar datos
    def actualizar(self, nombre=None, edad=None, direccion=None):
        if nombre:
            self.__nombre = nombre
        if edad:
            self.__edad = edad
        if direccion:
            self.__direccion = direccion

    # Método para borrar datos
    def borrar(self):
        self.__nombre = None
        self.__edad = None
        self.__direccion = None

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Dirección: {self.__direccion}"
