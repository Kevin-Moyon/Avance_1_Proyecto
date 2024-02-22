import os
import tempfile


def obtener_archivos_temporales():
    # Obtiene el directorio de archivos temporales del sistema
    directorio_temporal = tempfile.gettempdir()

    print("Directorio de archivos temporales:", directorio_temporal)

    # Obtiene la lista de archivos temporales
    archivos_temporales = os.listdir(directorio_temporal)

    if archivos_temporales:
        print("Archivos temporales encontrados:")
        for archivo in archivos_temporales:
            print(os.path.join(directorio_temporal, archivo))
    else:
        print("No se encontraron archivos temporales en el directorio.")


if __name__ == "__main__":
    obtener_archivos_temporales()
