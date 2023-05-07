class Materia:
    def __init__(self, dni, materia, fecha, nota, aprobacion):
        self.__dni = dni
        self.__materia = materia
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def __str__(self):
        return '%s %s %s %s %s' %(self.__dni, self.__materia, self.__fecha, self.__nota, self.__aprobacion)

    def getdni(self):
        return self.__dni
    
    def getmateria(self):
        return self.__materia
    
    def getfecha(self):
        return self.__fecha
    
    def getnota(self):
        return self.__nota
    
    def getaprobacion(self):
        return self.__aprobacion
