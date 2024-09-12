import os
import time
import schedule


def get_evil_files(directory, evil_extension):
    """
    Recorre el directorio y sus subcarpetas para encontrar archivos con la extensión maligna.
    Devuelve una lista de rutas de archivos malignos.
    """
    evil_files = []
    for root_dir, sub_dir, files in os.walk(directory):
        for file in files:
            if file.endswith(evil_extension):
                file_dir = os.path.join(root_dir, file)
                evil_files.append(file_dir)
    return evil_files

def delete_files(evil_files):
    """
    Elimina los archivos listados en evil_files.
    """
    for file in evil_files:
        try:
            os.remove(file)
            print(f"Archivo eliminado: {file}")
        except Exception as e:
            print(f"No se pudo eliminar {file}: {e}")

def scheduled_task():
    """
    Función que se ejecuta periódicamente para buscar y eliminar archivos malignos.
    """
    directory = "D:/test"
    evil_extension = ".pdf"
    evil_files = get_evil_files(directory, evil_extension)
    if evil_files:
        delete_files(evil_files)
    else:
        print("No se encontraron archivos malignos en este lote.")

# Función principal
if __name__ == "__main__":
    # Programar la tarea para que se ejecute cada minuto
    schedule.every(30).seconds.do(scheduled_task)

    print("Iniciando el programa. Presiona Ctrl+C para detenerlo.")

    while True:
        # Ejecuta las tareas programadas pendientes
        schedule.run_pending()
        # Pausa el bucle por 1 segundo para reducir el uso de CPU
        time.sleep(1)
