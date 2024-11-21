import time
import threading
import random
import tkinter as tk

# Clase que representa cada auto
class Auto:
    def __init__(self, id):
        self.id = id

# Clase que representa el estacionamiento
class Estacionamiento:
    def __init__(self, capacidad, canvas):
        self.capacidad = capacidad
        self.autos = []
        self.lock = threading.Lock()
        self.frecuencia_entrada = 1  # frecuencia inicial en segundos
        self.frecuencia_salida = 1   # frecuencia inicial en segundos
        self.canvas = canvas
        self.rectangulos = []  # Lista de objetos gráficos en el canvas

    def agregar_auto(self):
        while True:
            with self.lock:
                if len(self.autos) < self.capacidad:
                    nuevo_auto = Auto(len(self.autos) + 1)
                    self.autos.append(nuevo_auto)
                    self.dibujar_auto(len(self.autos) - 1)  # Dibujar auto en el canvas
                    print(f"Entrada: Auto {nuevo_auto.id} añadido.")
                else:
                    print("El estacionamiento está lleno. No se puede añadir más autos.")
            time.sleep(self.frecuencia_entrada)

    def retirar_auto(self):
        while True:
            with self.lock:
                if len(self.autos) > 0:
                    auto_retirado = self.autos.pop(0)
                    self.borrar_auto()  # Borrar auto del canvas
                    print(f"Salida: Auto {auto_retirado.id} retirado.")
                else:
                    print("El estacionamiento está vacío. No se pueden retirar autos.")
            time.sleep(self.frecuencia_salida)

    def cambiar_frecuencia_entrada(self, nueva_frecuencia):
        with self.lock:
            self.frecuencia_entrada = nueva_frecuencia
            print(f"Frecuencia de entrada cambiada a {nueva_frecuencia} segundos.")

    def cambiar_frecuencia_salida(self, nueva_frecuencia):
        with self.lock:
            self.frecuencia_salida = nueva_frecuencia
            print(f"Frecuencia de salida cambiada a {nueva_frecuencia} segundos.")

    def dibujar_auto(self, posicion):
        x = 10 + (posicion % 4) * 60
        y = 10 + (posicion // 4) * 60
        rect = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="blue")
        self.rectangulos.append(rect)

    def borrar_auto(self):
        if self.rectangulos:
            rect = self.rectangulos.pop(0)
            self.canvas.delete(rect)

# Función para ajustar la frecuencia de forma aleatoria
def ajustar_frecuencia(estacionamiento):
    while True:
        nueva_frecuencia_entrada = random.choice([0.5, 1, 2])
        nueva_frecuencia_salida = random.choice([0.5, 1, 2])
        estacionamiento.cambiar_frecuencia_entrada(nueva_frecuencia_entrada)
        estacionamiento.cambiar_frecuencia_salida(nueva_frecuencia_salida)
        time.sleep(5)  # Cambia frecuencias cada 5 segundos

# Función para crear la interfaz gráfica
def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Simulación de Estacionamiento")

    # Canvas para mostrar los autos
    canvas = tk.Canvas(ventana, width=260, height=200, bg="white")
    canvas.pack()

    # Instancia del estacionamiento
    estacionamiento = Estacionamiento(capacidad=12, canvas=canvas)
    
    # Crear hilos para entrada y salida de autos
    hilo_entrada = threading.Thread(target=estacionamiento.agregar_auto, daemon=True)
    hilo_salida = threading.Thread(target=estacionamiento.retirar_auto, daemon=True)
    hilo_frecuencia = threading.Thread(target=ajustar_frecuencia, args=(estacionamiento,), daemon=True)

    # Iniciar hilos
    hilo_entrada.start()
    hilo_salida.start()
    hilo_frecuencia.start()

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

# Ejecutar el programa con la interfaz gráfica
if __name__ == "__main__":
    iniciar_interfaz()
