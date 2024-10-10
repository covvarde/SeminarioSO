def fifo_scheduling(processes):
  """
  Ejecuta cada proceso sin ordenar la lista, mostrando el tiempo de inicio y finalización
  """
  current_time = 0
  
  for process in processes:
    start_time = current_time
    end_time = current_time + process[1]
    print(f"{process[0]}\t| Inicio: {start_time}s | Fin: {end_time}s")
    current_time = end_time


def sjf_scheduling(processes):
  """
  Ordena la lista de procesos según su duración, y los ejecuta mostrando el tiempo de inicio y finalización 
  """
  current_time = 0
  # Ordena la lista de acuerdo a la duración del proceso
  processes_sorted = sorted(processes, key=lambda x: x[1])
  
  for process in processes_sorted:
    start_time = current_time
    end_time = current_time + process[1]
    print(f"{process[0]}\t| Inicio: {start_time}s | Fin: {end_time}s")
    current_time = end_time


def priority_scheduling(processes):
  """
  Ordena la lista de procesos según su prioridad, y los ejecuta mostrando el tiempo de inicio y finalización 
  """
  current_time = 0
  processes_sorted = sorted(processes, key=lambda x: x[2])
  
  for process in processes_sorted:
    start_time = current_time
    end_time = current_time + process[1]
    print(f"{process[0]}\t| Inicio: {start_time}s | Fin: {end_time}s | Prioridad: {process[2]}")
    current_time = end_time


def round_robin(processes, quantum):
  """
  Ejecuta cada proceso únicamente durante el tiempo indicado, hasta finalizarlos. 
  La lista no se ordena antes de procesarse.
  """
  current_time = 0
  ready_queue = processes.copy()

  while ready_queue:
    process = ready_queue.pop(0)
    name, duration, _ = process
    if duration <= quantum:
      start_time = current_time
      end_time = current_time + duration
      print(f"{process[0]}\t| Inicio: {start_time}s | Fin: {end_time}s")
      current_time = end_time
    else:
      start_time = current_time
      end_time = current_time + quantum
      print(f"{process[0]}\t| Inicio: {start_time}s | Fin: {end_time}s")
      current_time = end_time
      ready_queue.append((name, duration - quantum, _))

def add_process(processes):
  """
  Recibe un nuevo proceso por consola y lo agrega a la lista.
  """
  name = input("\nNombre del proceso: ")
  duration = int(input("Duración del proceso: "))
  priority = int(input("Prioridad del proceso: "))

  new_process = (name, duration, priority)

  position = input("Agregar al inicio o al final de la lista? (I/F): ")
  if position.lower() == "i":
    processes.insert(0, new_process)  # Agrega al inicio
  else:
    processes.append(new_process)  # Agrega al final
  
  return processes

def main():
  """
  Lee los procesos del archivo inicial y ejecuta cada algoritmo.
  """
  processes = []
  with open("/procesos.txt", "r") as f:
    # Divide los elementos de cada proceso en Nombre, Duración y Prioridad
    for line in f:
      parts = line.strip().split(", ")
      processes.append((parts[0], int(parts[1]), int(parts[2])))

  while True:
    print("\nMenú:")
    print("1. Agregar proceso")
    print("2. Planificación FIFO")
    print("3. Planificación SJF")
    print("4. Planificación por prioridades")
    print("5. Planificación Round Robin")
    print("6. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
      processes = add_process(processes)
    elif option == "2":
      print("\nPlanificación FIFO:")
      fifo_scheduling(processes)
    elif option == "3":
      print("\nPlanificación SJF:")
      sjf_scheduling(processes)
    elif option == "4":
      print("\nPlanificación por prioridades:")
      priority_scheduling(processes)
    elif option == "5":
      print("\nPlanificación Round Robin:")
      round_robin(processes, 3)
    elif option == "6":
      break
    else:  
      print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
  main()
  
