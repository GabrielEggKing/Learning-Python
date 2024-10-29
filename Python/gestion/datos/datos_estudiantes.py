def obtener_datos_estudiante(estudiante):
    """Devuelve un diccionario con la información del estudiante."""
    nombre, rut, calificaciones, cursos = estudiante
    return {
        "Nombre": nombre,
        "Rut": rut,
        "Calificaciones": calificaciones,
        "Cursos": cursos
    }

def mostrar_datos_estudiante(estudiante):
    """Imprime la información del estudiante de manera legible."""
    datos = obtener_datos_estudiante(estudiante)
    print("\n--- Datos del Estudiante ---")
    for key, value in datos.items():
        print(f"{key}: {value}")

def calcular_promedio(calificaciones):
    """Calcula el promedio de las calificaciones de un estudiante."""
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def mostrar_promedio(estudiante):
    """Muestra el promedio de las calificaciones del estudiante."""
    nombre, rut, calificaciones, _ = estudiante
    promedio = calcular_promedio(calificaciones)
    print(f"Promedio de {nombre} ({rut}): {promedio:.2f}")
