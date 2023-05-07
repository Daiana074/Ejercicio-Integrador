from os import system
from manejadorAlumno import manejadorAlumno
from manejadorMateriaAprobada import manejadorMateriaAprobada
from claseAlumno import Alumno
from claseMateriaAprobada import Materia 

def menu():
    opcion = 0
    salir = False
    print('\n-----------MENU DE OPCIONES-----------')
    while not salir:
        print('\n1- Ver promedio y aplazos')
        print('\n2- Obtener informe de promociones')
        print('\n3- Obtener listado de alumnos')
        print('\n4 - Salir')
        opcion = int(input('\nIngrese opcion: '))

        #a.Leer por teclado el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos. 
        if(opcion == 1):
            dni = input('\nIngrese dni del alumno a buscar: ')
            notas = objetoMateria.buscar_notas(dni)
            print("Notas del alumno con DNI", dni, ":")
            print(notas)
            
            notas_aprobadas = []
            notas_ = []
            for nota in notas:
                if int(nota) >= 4:
                    notas_aprobadas.append(int(nota))
                notas_.append(int(nota))
            promedioSinAplazo = sum(notas_aprobadas) / len(notas_aprobadas)
            promedioConAplazo =  sum(notas_) / len(notas)
            print(f'Promedio sin aplazo: {promedioSinAplazo}')
            print(f'Promedio con aplazo: {promedioConAplazo}')
            system('pause')

       #nombre de una materia, e informar los estudiantes que la aprobaron en forma promocional, 
       #con nota mayor o igual que 7
        if(opcion == 2):
            nombreMat = input('\nIngrese nombre de la materia: ')
            info = objetoMateria.buscarAprobacion(nombreMat)
            print('Los estudiantes que aprobaron con Promocion son: ')
            print(info)
            dnis = []
            dnis = [r[0] for r in info]
            fechas = [r[1] for r in info]
            notass =[r[2] for r in info]
            print(dnis)
            print(fechas)
            print(notass)

            info2 = objetoAlumno.buscarAlumno(dnis)
            print('Los estudiantes que aprobaron con Promocion son: ')
            # print(info2)
                


            #print('DNI   Apellido y Nombre   Fecha   Nota   Año que cursa')
           
            # print(info2)
            system('pause')

        if(opcion == 3):
             print('\n------LISTADO DE ALUMNOS------\n')
             objetoAlumno.ordenar()
             print (Alumno.__gt__(objetoAlumno,objetoAlumno))
             #info3 = objetoAlumno.__gt
             system('pause')

        if(opcion == 4):
            salir = True

if __name__ == '__main__':
    
    objetoAlumno = manejadorAlumno(9)
    objetoAlumno.testManejador()

    objetoMateria = manejadorMateriaAprobada()
    objetoMateria.testManejador()


    menu()
