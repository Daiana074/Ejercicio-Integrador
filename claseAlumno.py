class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, añoCursado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__añoCursado = añoCursado

    def __str__(self):
        return '%s %s %s %s %s' % (self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__añoCursado)
    
    def getdni(self):
        return self.__dni
    
    def getapellido(self):
        return self.__apellido
    
    def getnombre(self):
        return self.__nombre
    
    def getcarrera(self):
        return self.__carrera
    
    def getañoCursadp(self):
        return self.__añoCursado
    
    def __gt__(self, otro):
        primero =str(self.__añoCursado) + str(self.__apellido) + str(self.__nombre)
       # segundo = str() + str(otro.__apellido) + str(otro.__nombre)
        return primero