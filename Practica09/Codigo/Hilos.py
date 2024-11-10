import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Movimiento de Imágenes")
ventana.geometry("600x400")  # Tamaño de la ventana

# Cargar las imágenes
imagen1 = Image.open("Hilos/imagen1.png")
imagen2 = Image.open("Hilos/imagen2.png")

# Redimensionar imágenes si es necesario
imagen1 = imagen1.resize((100, 100))
imagen2 = imagen2.resize((100, 100))

# Convertir a formato Tkinter
imagen1_tk = ImageTk.PhotoImage(imagen1)
imagen2_tk = ImageTk.PhotoImage(imagen2)

# Crear etiquetas para las imágenes
etiqueta_imagen1 = tk.Label(ventana, image=imagen1_tk)
etiqueta_imagen1.place(x=0, y=150)  # Posición inicial de la primera imagen

etiqueta_imagen2 = tk.Label(ventana, image=imagen2_tk)
etiqueta_imagen2.place(x=250, y=0)  # Posición inicial de la segunda imagen

# Variables para el movimiento
dx = 2  # Velocidad de movimiento en x para la primera imagen
dy = 2  # Velocidad de movimiento en y para la segunda imagen

# Función para mover las imágenes
def mover_imagenes():
    global dx, dy 

    # Obtener posiciones actuales
    x1, y1 = etiqueta_imagen1.winfo_x(), etiqueta_imagen1.winfo_y()
    x2, y2 = etiqueta_imagen2.winfo_x(), etiqueta_imagen2.winfo_y()
    
    # Mover imagen1 de izquierda a derecha
    if x1 + dx > ventana.winfo_width() - 100 or x1 < 0:
        # Invertir dirección si llega al borde
        dx = -dx
    etiqueta_imagen1.place(x=x1 + dx, y=y1)

    # Mover imagen2 de arriba a abajo
    if y2 + dy > ventana.winfo_height() - 100 or y2 < 0:
        # Invertir dirección si llega al borde
        dy = -dy
    etiqueta_imagen2.place(x=x2, y=y2 + dy)

    # Llamar a la función de nuevo después de 20 ms
    ventana.after(20, mover_imagenes)

# Iniciar el movimiento de las imágenes
mover_imagenes()

# Ejecutar la ventana principal
ventana.mainloop()
