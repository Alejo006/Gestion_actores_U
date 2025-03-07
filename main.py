from Estudiante import Estudiante
from Profesor import Profesor

# Listas para almacenar estudiantes y profesores
estudiantes = []
profesores = []

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    direccion = input("Ingrese la dirección del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    dia = input("Ingrese el día de clases del estudiante: ")

    estudiante = Estudiante(nombre, edad, direccion, curso, dia)
    estudiantes.append(estudiante)
    print("\nEstudiante registrado con éxito.\n")

def registrar_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    edad = int(input("Ingrese la edad del profesor: "))
    direccion = input("Ingrese la dirección del profesor: ")
    materia = input("Ingrese la materia que dicta: ")
    creditos = int(input("Ingrese la cantidad de créditos: "))
    codigo = input("Ingrese el código de la materia: ")

    profesor = Profesor(nombre, edad, direccion, materia, creditos, codigo)
    profesores.append(profesor)
    print("\nProfesor registrado con éxito.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
    else:
        print("\nLista de Estudiantes:")
        for i, estudiante in enumerate(estudiantes):
            print(f"{i + 1}. {estudiante}")

def mostrar_profesores():
    if not profesores:
        print("\nNo hay profesores registrados.\n")
    else:
        print("\nLista de Profesores:")
        for i, profesor in enumerate(profesores):
            print(f"{i + 1}. {profesor}")

def modificar_estudiante():
    mostrar_estudiantes()
    if not estudiantes:
        return

    index = int(input("\nIngrese el número del estudiante a modificar: ")) - 1
    if 0 <= index < len(estudiantes):
        nombre = input("Nuevo nombre (deje vacío para no cambiar): ")
        edad = input("Nueva edad (deje vacío para no cambiar): ")
        direccion = input("Nueva dirección (deje vacío para no cambiar): ")
        curso = input("Nuevo curso (deje vacío para no cambiar): ")
        dia = input("Nuevo día de clases (deje vacío para no cambiar): ")

        edad = int(edad) if edad else None
        estudiantes[index].actualizar(nombre or None, edad, direccion or None, curso or None, dia or None)
        print("\nEstudiante modificado con éxito.\n")
    else:
        print("\nNúmero inválido.\n")

def modificar_profesor():
    mostrar_profesores()
    if not profesores:
        return

    index = int(input("\nIngrese el número del profesor a modificar: ")) - 1
    if 0 <= index < len(profesores):
        nombre = input("Nuevo nombre (deje vacío para no cambiar): ")
        edad = input("Nueva edad (deje vacío para no cambiar): ")
        direccion = input("Nueva dirección (deje vacío para no cambiar): ")
        materia = input("Nueva materia (deje vacío para no cambiar): ")
        creditos = input("Nuevos créditos (deje vacío para no cambiar): ")
        codigo = input("Nuevo código (deje vacío para no cambiar): ")

        edad = int(edad) if edad else None
        creditos = int(creditos) if creditos else None
        profesores[index].actualizar(nombre or None, edad, direccion or None, materia or None, creditos, codigo or None)
        print("\nProfesor modificado con éxito.\n")
    else:
        print("\nNúmero inválido.\n")

def eliminar_estudiante():
    mostrar_estudiantes()
    if not estudiantes:
        return

    index = int(input("\nIngrese el número del estudiante a eliminar: ")) - 1
    if 0 <= index < len(estudiantes):
        estudiantes.pop(index)
        print("\nEstudiante eliminado con éxito.\n")
    else:
        print("\nNúmero inválido.\n")

def eliminar_profesor():
    mostrar_profesores()
    if not profesores:
        return

    index = int(input("\nIngrese el número del profesor a eliminar: ")) - 1
    if 0 <= index < len(profesores):
        profesores.pop(index)
        print("\nProfesor eliminado con éxito.\n")
    else:
        print("\nNúmero inválido.\n")

def menu():
    while True:
        print("\n📌 MENÚ PRINCIPAL")
        print("1 Registrar Estudiante")
        print("2 Registrar Profesor")
        print("3 Mostrar Estudiantes")
        print("4 Mostrar Profesores")
        print("5 Modificar Estudiante")
        print("6 Modificar Profesor")
        print("7 Eliminar Estudiante")
        print("8 Eliminar Profesor")
        print("9 Salir")

        opcion = input("\nElija una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_profesor()
        elif opcion == "3":
            mostrar_estudiantes()
        elif opcion == "4":
            mostrar_profesores()
        elif opcion == "5":
            modificar_estudiante()
        elif opcion == "6":
            modificar_profesor()
        elif opcion == "7":
            eliminar_estudiante()
        elif opcion == "8":
            eliminar_profesor()
        elif opcion == "9":
            print("\n ¡Gracias por usar el sistema!\n")
            break
        else:
            print("\n Opción inválida. Intente de nuevo.\n")

# Ejecutar el menú
menu()
