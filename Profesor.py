from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, materia,creditos,codigo):
        super().__init__(nombre, edad, direccion)
        self.__materia=materia
        self.__creditos=creditos
        self.__codigo=codigo

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









    def __str__(self):
        print(f"Los datos del profesor son los siguiente: \n", super().__str__(), "\n que dicta la meteria de: ", self.getmateria, "\n y tiene los siguinets creditos: ", self.getcreditos, "\n el codigo de la materia es: ", self.getcodigos)