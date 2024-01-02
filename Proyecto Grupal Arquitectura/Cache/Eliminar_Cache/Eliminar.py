import ctypes
from Cache import Datos_Cache

def mostrar_informacion_cache():
    print("\nInformación de la caché L2:")
    Datos_Cache.obtener_informacion_cache()

def borrar_cache():
    respuesta = input("\n¿Desea limpiar la caché del sistema? (s/n): ").lower()
    if respuesta == 's':
        try:
            ctypes.windll.kernel32.SetSystemFileCacheSize(-1, -1, 0)
            print("Caché del sistema eliminada exitosamente.")
        except Exception as e:
            print(f"Error al intentar eliminar la caché del sistema: {e}")
    else:
        print("No se eliminó la caché del sistema.")