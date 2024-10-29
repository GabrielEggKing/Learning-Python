import json
import os

estudiantes = []

def agregar_estudiante(nombre, matricula, rut):
    estudiante = {
        "nombre": nombre,
        "matricula": matricula,
        "rut": rut
    }
    estudiantes.append(estudiante)
    print("Estudiante agregado con éxito.")

def consultar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- Lista de Estudiantes ---")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, RUT: {estudiante['rut']}")

def actualizar_estudiante(matricula, nuevo_nombre=None, nuevo_rut=None):
    for estudiante in estudiantes:
        if estudiante["matricula"] == matricula:
            if nuevo_nombre:
                estudiante["nombre"] = nuevo_nombre
            if nuevo_rut:
                estudiante["rut"] = nuevo_rut
            print("Estudiante actualizado con éxito.")
            return
    print("Estudiante no encontrado.")

def eliminar_estudiante(matricula):
    for estudiante in estudiantes:
        if estudiante["matricula"] == matricula:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return
    print("Estudiante no encontrado.")