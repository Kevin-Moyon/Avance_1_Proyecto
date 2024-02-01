import os

def obtener_archivos_secuenciales(directorio):
    try:
        # Obtiene la lista de archivos en el directorio
        archivos = [archivo for archivo in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, archivo))]

        # Ordena la lista alfabéticamente
        archivos.sort()
        print("")
        print(f"Archivos secuenciales en {directorio}:")
        for archivo in archivos:
            print(os.path.join(directorio, archivo))

    except FileNotFoundError:
        print(f"El directorio {directorio} no existe.")
    except Exception as e:
        print(f"Error al obtener archivos secuenciales: {e}")

if __name__ == "__main__":
    # Especifica el directorio que deseas analizar
    directorio_a_analizar = os.path.expanduser("~") #Directorio de la secuencia de creacion de Usuario

    obtener_archivos_secuenciales(directorio_a_analizar)
