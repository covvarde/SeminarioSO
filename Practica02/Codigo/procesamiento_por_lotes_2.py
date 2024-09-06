import os
import schedule
import time

def obtener_archivos_malignos(directorio, extension_maligna):
    """
    Recorre el directorio y sus subcarpetas para encontrar archivos con la extensión maligna.
    Devuelve una lista de rutas de archivos malignos.
    """
    archivos_malignos = []
    for carpeta_raiz, subcarpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension_maligna):
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                archivos_malignos.append(ruta_archivo)
    return archivos_malignos

def eliminar_archivos_lote(archivos_malignos):
    """
    Elimina los archivos listados en archivos_malignos.
    """
    for archivo in archivos_malignos:
        try:
            os.remove(archivo)
            print(f"Archivo eliminado: {archivo}")
        except Exception as e:
            print(f"No se pudo eliminar {archivo}: {e}")

def tarea_programada():
    """
    Función que se ejecuta periódicamente para buscar y eliminar archivos malignos.
    """
    directorio = "ruta/de/tu/carpeta"  # Cambia esto a la ruta de tu carpeta
    extension_maligna = ".maligno"  # Cambia esto a la extensión que desees identificar como maligna
    archivos_malignos = obtener_archivos_malignos(directorio, extension_maligna)
    if archivos_malignos:
        eliminar_archivos_lote(archivos_malignos)
    else:
        print("No se encontraron archivos malignos en este lote.")

# Programar la tarea para que se ejecute cada minuto
schedule.every(1).minute.do(tarea_programada)

print("Iniciando el programa. Presiona Ctrl+C para detenerlo.")
while True:
    # Ejecuta las tareas programadas pendientes
    schedule.run_pending()
    # Pausa el bucle por 1 segundo para reducir el uso de CPU
    time.sleep(1)
