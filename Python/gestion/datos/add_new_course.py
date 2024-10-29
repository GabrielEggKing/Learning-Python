cursos = []

def agregar_curso(nombre_curso):
    """Agrega un nuevo curso a la lista de cursos."""
    if not nombre_curso.strip():
        print("Error: El nombre del curso no puede estar vacío.")
        return


    if nombre_curso in cursos:
        print(f"El curso '{nombre_curso}' ya está registrado.")
        return

    cursos.append(nombre_curso)
    print(f"Curso '{nombre_curso}' agregado exitosamente.")

def mostrar_cursos():
    """Muestra todos los cursos registrados."""
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\n--- Cursos Registrados ---")
        for curso in cursos:
            print(f"- {curso}")

