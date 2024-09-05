def process_line(line):
    # Dividir la línea en dos partes usando '/' como delimitador
    prefix, suffix = line.strip().split('/', 1)

    # Procesar la primera parte
    # Dividir los números hexadecimales por ':'
    hex_parts = prefix.split(':')

    # Convertir números hexadecimales a decimales
    decimal_numbers = [int(number, 16) for number in hex_parts]

    # Procesar la segunda parte
    # Dividir la segunda parte por comas
    parts = suffix.strip().split(',')

    # La segunda cadena de texto
    second_string = parts[2]

    # Dividir los números decimales por '.'
    decimal_numbers_from_suffix = parts[5].split('.')

    # Convertir números decimales a hexadecimales
    hex_numbers = [format(int(number), 'X') for number in decimal_numbers_from_suffix]

    # Crear el formato de salida
    decimal_numbers_str = ' : '.join(map(str, decimal_numbers))
    hex_numbers_str = '.'.join(hex_numbers)

    output_line = f"{second_string} : {decimal_numbers_str} : {hex_numbers_str}\n"

    return output_line

def read_and_process_file(input_filename, output_filename, batch_size=100):
    # Crear una lista vacía para almacenar las líneas procesadas
    processed_lines = []

    try:
        # Abrir el archivo de entrada por lotes en modo lectura
        with open(input_filename, 'r') as infile:
            batch = []
            
            for line in infile:
                batch.append(line)

                if len(batch) >= batch_size:
                    # Procesar el lote actual
                    processed_lines.extend([process_line(l) for l in batch if process_line(l) is not None])
                    
                    # Limpiar el lote para el siguiente grupo
                    batch = []

            # Procesar el último lote si tiene datos
            if batch:
                processed_lines.extend([process_line(l) for l in batch if process_line(l) is not None])
        
        # Escribir todos los resultados en el archivo de salida final
        with open(output_filename, 'w') as outfile:
            for pline in processed_lines:
                outfile.write(pline)
    
    # Excepciones
    except FileNotFoundError:
        print(f"Error: El archivo '{input_filename}' no fue encontrado.")
    except IOError as e:
        print(f"Error: Ocurrió un IOError. Detalles: {e}")
    except Exception as e:
        print(f"Error durante el procesamiento: {e}")

# Función principal
if __name__ == "__main__":
    input_filename = 'prueba2.txt'
    output_filename = 'output.txt'
    
    # Llamada al proceso principal
    read_and_process_file(input_filename, output_filename, batch_size=100)
