import os

def obtener_archivos_espaciales(directorio, cantidad_archivos=5):
    try:
        # Obtiene la lista de archivos en el directorio
        archivos = [(os.path.join(directorio, archivo), os.path.getsize(os.path.join(directorio, archivo)))
                    for archivo in os.listdir(directorio)]

        # Ordena la lista de archivos por tamaño de mayor a menor
        archivos.sort(key=lambda x: x[1], reverse=True)
        print("")
        print(f"{cantidad_archivos} archivos más grandes en {directorio}:")
        for i in range(min(cantidad_archivos, len(archivos))):
            print(f"{archivos[i][0]} - Tamaño: {archivos[i][1]} bytes")

    except FileNotFoundError:
        print(f"El directorio {directorio} no existe.")
    except Exception as e:
        print(f"Error al obtener archivos espaciales: {e}")

if __name__ == "__main__":
    # Especifica el directorio que deseas analizar
    directorio_a_analizar = os.getcwd()  #Directorio en el que trabajo

    # Especifica la cantidad de archivos más grandes que deseas mostrar
    cantidad_archivos_mostrar = 5

    obtener_archivos_espaciales(directorio_a_analizar, cantidad_archivos_mostrar)
