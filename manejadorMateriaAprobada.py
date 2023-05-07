import csv 
from claseMateriaAprobada import Materia 

class manejadorMateriaAprobada:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for MateriaAprobada in self.__lista:
            s += str(MateriaAprobada) + '\n'
        return s
    
    def agregar(self, objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        archi = open('materiasAprobadas.csv')
        reader = csv.reader(archi,delimiter = ';')
        for i in reader:
            dni = i[0]
            materia = i[1]
            fecha = i[2]
            nota = i[3]
            aprobacion = i[4]
            objeto = Materia(dni,materia,fecha,nota,aprobacion)
            self.agregar(objeto)
        archi.close()

  
    def buscar_notas(self, dni):
        notas = []
        for materia in self.__lista:
            if materia.getdni() == dni:
                notas.append(materia.getnota())
        return notas
    
    #ejercicio c
    def __lt__(self, other):
        if self.getanio() < other.getanio():
            return True
        elif self.getanio() == other.getanio():
            if self.getapellido() < other.getapellido():
                return True
            elif self.getapellido() == other.getapellido():
                if self.getnombre() < other.getnombre():
                    return True
        return False



     # def promocionales(alumnos, materiasaprobadas):
    #     mat = input("Ingrese nombre de materia > ")
    #     print("DNI - Apellido y nombre - Fecha - Nota - Año que cursa")
    #     for i in range(len(materiasaprobadas)):
    #         if (mat == materiasaprobadas[i].getNomb()) and (materiasaprobadas[i].getNota() >= 7):
    #             dni = materiasaprobadas[i].getDNI()
    #             id = manejadorAl.obtenerAlumno(alumnos, dni)
    #             print(alumnos[id].getDNI(), " - ", alumnos[id].getNyA(), " - ", materiasaprobadas[i].getFecha(), " - ", materiasaprobadas[i].getNota(), " - ", alumnos[id].getAAAA())



    # def buscarAprobacion(self, nombreMat):
    #     promdni = []
    #     promfecha = []
    #     promnota = []
    #     for materia in self.__lista:
    #         if materia.getmateria() == nombreMat:
    #             if materia.getaprobacion() == 'P':
    #                 promdni.append(materia.getdni())
    #                 promfecha.append(materia.getfecha())
    #                 promnota.append(materia.getnota())
    
    # def buscarAprobacion(self, nombreMat):
    #     resultados = []
    #     for materia in self.__lista:
    #         if materia.getmateria() == nombreMat and materia.getaprobacion() == 'P':
    #             resultados.append([materia.getdni(), materia.getfecha(), materia.getnota()])
    #     return resultados

    
    
        
    
    