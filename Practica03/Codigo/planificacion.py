def fifo_scheduling(processes):
  """
  Agrega cada proceso a una lista usando FIFO, inclyendo el tiempo de inicio y finalizacion
  """
  current_time = 0
  schedule = []
  for process in processes:
    start_time = current_time
    end_time = current_time + process[1]
    schedule.append((process[0], start_time, end_time))
    current_time = end_time
  return schedule


def sjf_scheduling(processes):
  """
  Agrega cada proceso a una lista, ordenada según su duración, incluyendo el tiempo de inicio y finalizació 
  """
  current_time = 0
  schedule = []
  # Ordena la lista de acuerdo a la duración del proceso
  processes_sorted = sorted(processes, key=lambda x: x[1])
  for process in processes_sorted:
    start_time = current_time
    end_time = current_time + process[1]
    schedule.append((process[0], start_time, end_time))
    current_time = end_time
  return schedule


def main():
  """
  Lee los procesos del archivo inicial y los procesa
  """
  processes = []
  with open("/procesos.txt", "r") as f:
    # Divide los elementos de cada proceso en Nombre, Duración y Prioridad
    for line in f:
      parts = line.strip().split(", ")
      processes.append((parts[0], int(parts[1]), int(parts[2])))

  print("Planificación FIFO:")
  for process in fifo_scheduling(processes):
    print(f"{process[0]}: Inicio = {process[1]}s, Fin = {process[2]}s")

  print("\nPlanificación SJF:")
  for process in sjf_scheduling(processes):
    print(f"{process[0]}: Inicio = {process[1]}s, Fin = {process[2]}s")


if __name__ == "__main__":
  main()
