import json
import os

# Tupla que almacena la información de la universidad
universidad = ("Universidad APLAPLAC", "Concepción", 10)  # (nombre, sede, número de programas)

# Ruta del archivo JSON para persistir información sobre la universidad
universidad_path = 'gestion/db_sys/datos_universidad.json'

# Inicialización del archivo de la universidad si no existe
def inicializar_universidad():
    if not os.path.exists('gestion/db_sys'):
        os.makedirs('gestion/db_sys')
    if not os.path.exists(universidad_path):
        guardar_universidad()

# Guardar información de la universidad en un archivo JSON
def guardar_universidad():
    datos = {
        "nombre": universidad[0],
        "sede": universidad[1],
        "programas": universidad[2]
    }
    with open(universidad_path, 'w') as file:
        json.dump(datos, file, indent=4)

# Consultar información de la universidad
def consultar_universidad():
    print(f"Nombre: {universidad[0]}")
    print(f"Sede: {universidad[1]}")
    print(f"Número de Programas: {universidad[2]}")

# Inicializar universidad al cargar el módulo
inicializar_universidad()

