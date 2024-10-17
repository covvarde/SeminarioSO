# Algoritmo Primer Ajuste
def first_fit(archivos, bloques_memoria):
    asignaciones = [-1] * len(archivos)
    for i, archivo in enumerate(archivos):
        for j, bloque in enumerate(bloques_memoria):
            if archivo[1] <= bloque:
                asignaciones[i] = j
                bloques_memoria[j] -= archivo[1]
                break
    return asignaciones

# Algoritmo Mejor Ajuste
def best_fit(archivos, bloques_memoria):
    asignaciones = [-1] * len(archivos)
    for i, archivo in enumerate(archivos):
        mejor_bloque = -1
        for j, bloque in enumerate(bloques_memoria):
            if archivo[1] <= bloque:
                if mejor_bloque == -1 or bloques_memoria[mejor_bloque] > bloque:
                    mejor_bloque = j
        if mejor_bloque != -1:
            asignaciones[i] = mejor_bloque
            bloques_memoria[mejor_bloque] -= archivo[1]
    return asignaciones

# Algoritmo Peor Ajuste
def worst_fit(archivos, bloques_memoria):
    asignaciones = [-1] * len(archivos)
    for i, archivo in enumerate(archivos):
        peor_bloque = -1
        for j, bloque in enumerate(bloques_memoria):
            if archivo[1] <= bloque:
                if peor_bloque == -1 or bloques_memoria[peor_bloque] < bloque:
                    peor_bloque = j
        if peor_bloque != -1:
            asignaciones[i] = peor_bloque
            bloques_memoria[peor_bloque] -= archivo[1]
    return asignaciones

# Algoritmo Siguiente Ajuste
def next_fit(archivos, bloques_memoria):
    asignaciones = [-1] * len(archivos)
    posicion_actual = 0
    for i, archivo in enumerate(archivos):
        for j in range(len(bloques_memoria)):
            if archivo[1] <= bloques_memoria[posicion_actual]:
                asignaciones[i] = posicion_actual
                bloques_memoria[posicion_actual] -= archivo[1]
                break
            posicion_actual = (posicion_actual + 1) % len(bloques_memoria)
    return asignaciones

# Función para imprimir las asignaciones
def imprimir_asignaciones(archivos, bloques_memoria, asignaciones, algoritmo):
    print("\nBloques de memoria iniciales:", bloques_memoria)

    print(f"\n\tResultados de {algoritmo}:")
    for i, asignacion in enumerate(asignaciones):
        archivo_nombre = archivos[i][0]
        archivo_tamaño = archivos[i][1]
        if asignacion != -1:
            bloque_tamaño = bloques_memoria[asignacion]
            print(f"Archivo {archivo_nombre} ({archivo_tamaño}kb) asignado al bloque de {bloque_tamaño}kb")
        else:
            print(f"Archivo {archivo_nombre} ({archivo_tamaño}kb) no se pudo asignar")

# Función para agregar un archivo a la lista
def agregar_archivo(archivos):
    nombre = input("Ingresa el nombre del archivo: ")
    tamaño = int(input("Ingresa el tamaño del archivo (en KB): "))
    posicion = input("¿Agregar al inicio o al final? (I/F): ").strip().lower()

    if posicion == 'i':
        archivos.insert(0, (nombre, tamaño))
    else:
        archivos.append((nombre, tamaño))
    print(f"Archivo {nombre} ({tamaño}kb) agregado a la lista.")

# Función para agregar un nuevo espacio de memoria
def agregar_espacio_memoria(bloques_memoria):
    tamaño = int(input("Ingresa el tamaño del nuevo bloque de memoria (en KB): "))
    estado = input("¿El bloque está ocupado o disponible? (O/D): ").strip().lower()
    
    # Si el bloque está ocupado, se representa con tamaño 0
    bloque = tamaño if estado == 'd' else 0
    posicion = input("¿Agregar al inicio o al final? (I/F): ").strip().lower()

    if posicion == 'i':
        bloques_memoria.insert(0, bloque)
    else:
        bloques_memoria.append(bloque)
    print(f"Bloque de {tamaño}kb ({'ocupado' if bloque == 0 else 'disponible'}) agregado a la lista.")

# Simulación con un archivo de entrada y bloques de memoria predefinidos
def main(archivo, bloques_memoria):
    archivos = []
    with open(archivo, 'r') as f:
        for linea in f:
            nombre, tamaño = linea.split(',')
            archivos.append((nombre.strip(), int(tamaño.strip().replace('kb', ''))))

    while True:
      print("\nMenú:")
      print("1. Agregar archivo")
      print("2. Agregar espacio de memoria")
      print("3. Primer ajuste")
      print("4. Mejor ajuste")
      print("5. Peor ajuste")
      print("6. Siguiente ajuste")
      print("7. Salir")

      option = input("Seleccione una opción: ")

      if option == "1":
        agregar_archivo(archivos)
      elif option == "2":
        agregar_espacio_memoria(bloques_memoria)
      elif option == "3":
        bloques_ff = bloques_memoria[:]
        asignaciones_ff = first_fit(archivos, bloques_ff)
        imprimir_asignaciones(archivos, bloques_memoria, asignaciones_ff, "Primer Ajuste")
      elif option == "4":
        bloques_bf = bloques_memoria[:]
        asignaciones_bf = best_fit(archivos, bloques_bf)
        imprimir_asignaciones(archivos, bloques_memoria, asignaciones_bf, "Mejor Ajuste")
      elif option == "5":
        bloques_wf = bloques_memoria[:]
        asignaciones_wf = worst_fit(archivos, bloques_wf)
        imprimir_asignaciones(archivos, bloques_memoria, asignaciones_wf, "Peor Ajuste")
      elif option == "6":
        bloques_nf = bloques_memoria[:]
        asignaciones_nf = next_fit(archivos, bloques_nf)
        imprimir_asignaciones(archivos, bloques_memoria, asignaciones_nf, "Siguiente Ajuste")
      elif option == "7":
        break
      else:  
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
  archivo_entrada = 'archivos.txt'
  bloques_memoria = [1000, 400, 1800, 700, 900, 1200, 1500]

  main(archivo_entrada, bloques_memoria)
