import numpy as np
import csv 
from claseAlumno import Alumno

class manejadorAlumno:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension, incremento=1):
        self.__Alumno = np.empty(dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ''
        for Alumno in self.__Alumno:
            s += str(Alumno) + '\n'
        return s
    
    def agregarAlumno(self, alumno):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Alumno.resize(self.__dimension)
        self.__Alumno[self.__cantidad] = alumno
        self.__cantidad += 1

    def testManejador(self):
        archi = open('alumnos.csv')
        reader = csv.reader(archi,delimiter=';')
        for i in reader:
            dni = i[0]
            apellido = i[1]
            nombre = i[2]
            carrera = i[3]
            añoCursado = i[4]
            objeto = Alumno(dni, apellido, nombre, carrera, añoCursado)
            self.agregarAlumno(objeto)
        archi.close()
    
    #c
    def ordenar(self):
        intercambio=True
        while intercambio:
            intercambio=False
            for i in range (len(self.__Alumno)-1):
                if(self.__Alumno[i]>self.__Alumno[i+1]):
                    self.__Alumno[i],self.__Alumno[i+1]=self.__Alumno[i+1],self.__Alumno[i]
                    intercambio=True
    # obtenerAlumno(alumnos, dni):
    #     i = 0
    #     band = False
    #     while i < len(alumnos) and band == False:
    #         if(dni == alumnos[i].getDNI()):
    #             band = True
    #         i += 1 
    #     return i
        
    # def promocionales(alumnos, materiasaprobadas):
    #     mat = input("Ingrese nombre de materia > ")
    #     print("DNI - Apellido y nombre - Fecha - Nota - Año que cursa")
    #     for i in range(len(materiasaprobadas)):
    #         if (mat == materiasaprobadas[i].getNomb()) and (materiasaprobadas[i].getNota() >= 7):
    #             dni = materiasaprobadas[i].getDNI()
    #             id = manejadorAl.obtenerAlumno(alumnos, dni)
    #             print(alumnos[id].getDNI(), " - ", alumnos[id].getNyA(), " - ", materiasaprobadas[i].getFecha(), " - ", materiasaprobadas[i].getNota(), " - ", alumnos[id].getAAAA())

    #appelido y nombre y año que cursa necesito
    # def buscarAlumno(self, dnis):
    #     info2 = []
    #     for Alumno in self.__Alumno:
            
    #             if(Alumno.getdni() == ):
    #                 info2.append([Alumno.getapellido(), Alumno.getnombre(), Alumno.getañoCursado()])
    #             return info2

    #     #     def buscarAprobacion(self, nombreMat):
    #     # resultados = []
    #     # for materia in self.__lista:
    #     #     if materia.getmateria() == nombreMat and materia.getaprobacion() == 'P':
    #     #         resultados.append([materia.getdni(), materia.getfecha(), materia.getnota()])
    #     # return resultados    

                 
    