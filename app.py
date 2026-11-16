import os
import pandas as pd

def procesar_datos():
    # 1. Obtener rutas desde variables de entorno (con valores por defecto por si acaso)
    input_path = os.getenv('INPUT_FILE', '/data/input/datos.csv')
    output_path = os.getenv('OUTPUT_FILE', '/data/output/resultado.csv')

    print(f"Iniciando procesamiento...")
    print(f"Ruta de entrada configurada: {input_path}")
    print(f"Ruta de salida configurada: {output_path}")
    
    try:
        # 2. Leer los datos de entrada
        df = pd.read_csv(input_path)
        
        # 3. Procesamiento: Generar estadísticas descriptivas de los datos numéricos
        resumen = df.describe()
        
        # 4. Crear el directorio de salida si no existe para evitar errores
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 5. Escribir el archivo de salida
        resumen.to_csv(output_path)
        print(f"Procesamiento exitoso. Archivo guardado en {output_path}")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de entrada en {input_path}")
        exit(1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        exit(1)

if __name__ == '__main__':
    procesar_datos()