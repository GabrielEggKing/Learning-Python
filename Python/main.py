import tkinter as tk
from tkinter import messagebox, simpledialog
from gestion.gestion_estudiante import agregar_estudiante, consultar_estudiantes, actualizar_estudiante, eliminar_estudiante
from gestion.gestion_cursos import agregar_curso
from gestion.gestion_universidad import consultar_universidad
from gestion.datos.datos_estudiantes import mostrar_datos_estudiante, mostrar_promedio
from gestion.datos.calificaciones import agregar_calificacion, consultar_calificaciones, mostrar_promedio_estudiante
from gestion.datos.add_new_course import mostrar_cursos

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Gestionar Estudiantes")
    print("2. Gestionar Cursos")
    print("3. Consultar Universidad")
    print("4. Consultar Calificaciones")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                print("\n--- Gestión de Estudiantes ---")
                print("1. Agregar Estudiante")
                print("2. Consultar Estudiantes")
                print("3. Actualizar Estudiante")
                print("4. Eliminar Estudiante")
                print("5. Volver al Menú Principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == '1':
                    # Solicita los datos del estudiante para agregar
                    nombre = input("Ingrese el nombre del estudiante: ")
                    matricula = input("Ingrese la matrícula del estudiante: ")
                    rut = input("Ingrese el RUT del estudiante: ")
                    agregar_estudiante(nombre, matricula, rut)
                    
                elif sub_opcion == '2':
                    consultar_estudiantes()
                    
                elif sub_opcion == '3':
                    # Solicita los datos para actualizar al estudiante
                    matricula = input("Ingrese la matrícula del estudiante a actualizar: ")
                    nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para no cambiar): ")
                    nuevo_rut = input("Ingrese el nuevo RUT (o presione Enter para no cambiar): ")
                    actualizar_estudiante(matricula, nuevo_nombre if nuevo_nombre else None, nuevo_rut if nuevo_rut else None)
                    
                elif sub_opcion == '4':
                    # Solicita la matrícula del estudiante para eliminar
                    matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
                    eliminar_estudiante(matricula)
                    
                elif sub_opcion == '5':
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == '2':
            while True:
                print("\n--- Gestión de Cursos ---")
                print("1. Agregar Curso")
                print("2. Mostrar Cursos")
                print("3. Volver al Menú Principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == '1':
                    nombre_curso = input("Ingrese el nombre del curso: ")
                    agregar_curso(nombre_curso)
                    
                elif sub_opcion == '2':
                    mostrar_cursos()
                    
                elif sub_opcion == '3':
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == '3':
            while True:    
                print("\n--- Consultar Universidad ---")
                consultar_universidad()
                print("1. Volver al Menú Principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == '1':
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == '4':
            while True:
                print("\n--- Gestión de Calificaciones ---")
                print("1. Agregar Calificación")
                print("2. Consultar Calificaciones")
                print("3. Mostrar Promedio de Estudiante")
                print("4. Volver al Menú Principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == '1':
                    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
                    calificacion = float(input("Ingrese la calificación (1.0 - 7.0): "))
                    agregar_calificacion(nombre_estudiante, calificacion)
                    
                elif sub_opcion == '2':
                    consultar_calificaciones()
                    
                elif sub_opcion == '3':
                    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
                    mostrar_promedio_estudiante(nombre_estudiante)
                    
                elif sub_opcion == '4':
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == '5':
            print("¡Adiós!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()