import tkinter as tk
from tkinter import scrolledtext
import threading
import time

# Semáforos y variables compartidas
mutex = threading.Semaphore(1)
write_sem = threading.Semaphore(1)
read_count = 0

# Archivo simulado
archivo = ["Este es el contenido inicial del archivo.\n"]

def leer_archivo(textbox):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:  # Primer lector bloquea escritura
        write_sem.acquire()
    mutex.release()

    for linea in archivo:
        for char in linea:
            time.sleep(0.1)  # Simula delay por carácter
            textbox.insert(tk.END, char)
        textbox.insert(tk.END, "\n")

    mutex.acquire()
    read_count -= 1
    if read_count == 0:  # Último lector libera escritura
        write_sem.release()
    mutex.release()

def editar_archivo(textbox, nueva_linea):
    write_sem.acquire()
    time.sleep(1)  # Simula tiempo de escritura
    archivo.append(nueva_linea + "\n")
    textbox.insert(tk.END, "Contenido editado guardado.\n")
    write_sem.release()

def guardar_archivo(textbox):
    write_sem.acquire()
    time.sleep(1)  # Simula tiempo de guardado
    with open("archivo_simulado.txt", "w") as file:
        file.writelines(archivo)
    textbox.insert(tk.END, "Archivo guardado en archivo_simulado.txt.\n")
    write_sem.release()

# Funciones asociadas a botones
def iniciar_lectura(textbox):
    textbox.delete(1.0, tk.END)
    threading.Thread(target=leer_archivo, args=(textbox,)).start()

def iniciar_edicion(textbox, entrada):
    threading.Thread(target=editar_archivo, args=(textbox, entrada.get())).start()

def iniciar_guardado(textbox):
    threading.Thread(target=guardar_archivo, args=(textbox,)).start()

# Configuración de la interfaz gráfica
def crear_ventana(nombre_proceso):
    ventana = tk.Toplevel()
    ventana.title(nombre_proceso)
    ventana.geometry("500x400")

    texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=20)
    texto.pack(pady=10)

    if nombre_proceso == "Leer":
        btn_leer = tk.Button(ventana, text="Leer", command=lambda: iniciar_lectura(texto))
        btn_leer.pack()
    elif nombre_proceso == "Editar":
        entrada = tk.Entry(ventana, width=40)
        entrada.pack(pady=5)
        btn_editar = tk.Button(ventana, text="Editar", command=lambda: iniciar_edicion(texto, entrada))
        btn_editar.pack()
    elif nombre_proceso == "Guardar":
        btn_guardar = tk.Button(ventana, text="Guardar", command=lambda: iniciar_guardado(texto))
        btn_guardar.pack()

# Ventana principal
root = tk.Tk()
root.title("Simulación de archivo con lectores y escritores")
root.geometry("300x200")

btn_lector = tk.Button(root, text="Abrir Lector", command=lambda: crear_ventana("Leer"))
btn_lector.pack(pady=10)

btn_editor = tk.Button(root, text="Abrir Editor", command=lambda: crear_ventana("Editar"))
btn_editor.pack(pady=10)

btn_guardar = tk.Button(root, text="Abrir Guardador", command=lambda: crear_ventana("Guardar"))
btn_guardar.pack(pady=10)

root.mainloop()
