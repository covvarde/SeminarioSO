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

  print("Planificación FIFO:")
  fifo_scheduling(processes)

  print("\nPlanificación SJF:")
  sjf_scheduling(processes)

  print("\nPlanificación por prioridades:")
  priority_scheduling(processes)

  print("\nPlanificación Round Robin:")
  round_robin(processes, 3)


if __name__ == "__main__":
  main()
