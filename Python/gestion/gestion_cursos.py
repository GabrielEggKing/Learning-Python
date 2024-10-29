cursos = []

def agregar_curso(nombre_curso):
    if nombre_curso not in cursos:
        cursos.append(nombre_curso)
        print("Curso agregado con éxito.")
    else:
        print("El curso ya está registrado.")

def mostrar_cursos():
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\n--- Lista de Cursos ---")
        for curso in cursos:
            print(f"- {curso}")
