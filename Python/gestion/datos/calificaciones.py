calificaciones = {}

def agregar_calificacion(nombre_estudiante, calificacion):
    if 1.0 <= calificacion <= 7.0:
        if nombre_estudiante not in calificaciones:
            calificaciones[nombre_estudiante] = []
        calificaciones[nombre_estudiante].append(calificacion)
        print("Calificación agregada con éxito.")
    else:
        print("La calificación debe estar entre 1.0 y 7.0.")

def consultar_calificaciones():
    if not calificaciones:
        print("No hay calificaciones registradas.")
    else:
        print("\n--- Calificaciones de Estudiantes ---")
        for estudiante, notas in calificaciones.items():
            print(f"{estudiante}: {notas}")

def mostrar_promedio_estudiante(nombre_estudiante):
    if nombre_estudiante in calificaciones and calificaciones[nombre_estudiante]:
        promedio = sum(calificaciones[nombre_estudiante]) / len(calificaciones[nombre_estudiante])
        print(f"El promedio de {nombre_estudiante} es: {promedio:.2f}")
    else:
        print(f"No hay calificaciones registradas para el estudiante: {nombre_estudiante}")


