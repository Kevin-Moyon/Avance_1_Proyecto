import psutil
import cpuinfo
import subprocess
from Cache import Datos_Cache
import ctypes

# Obtener la cantidad de memoria disponible
memoria_disponible = psutil.virtual_memory().available / (1024 * 1024)

# Obtener el porcentaje de uso de la memoria
memoria_usada = psutil.virtual_memory().percent

# Obtener el rendimiento de la red
rendimiento_red = psutil.net_io_counters().bytes_sent / (1024 * 1024)

# Obtener la temperatura del CPU (solo disponible en algunas plataformas)
try:
    temperatura_cpu = psutil.sensors_temperatures()['coretemp'][0].current
except AttributeError:
    temperatura_cpu = "No disponible en esta plataforma"

# Obtener información general sobre la CPU usando cpuinfo
info_cpu = cpuinfo.get_cpu_info()

# Obtener el tamaño de la caché L3 en sistemas Windows usando wmic
def obtener_tamano_cache():
    try:
        salida = subprocess.check_output(["wmic", "cpu", "get", "L3CacheSize"]).decode("utf-8")
        lineas = salida.split('\n')
        for linea in lineas:
            if "L3 Cache Size" in linea:
                return linea.split()[-1]
    except subprocess.CalledProcessError:
        pass
    return "No disponible"

# Obtener el tamaño de la caché L3
tamaño_cache = obtener_tamano_cache()

# Imprimir la cantidad de memoria disponible, el porcentaje de uso de la memoria, el rendimiento de la red, la temperatura del CPU y detalles de la CPU
print(f"Memoria disponible: {memoria_disponible:.2f} MB")
print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
print(f"Temperatura del CPU: {temperatura_cpu}")
print(f"Información de la CPU: {info_cpu}")
print(f"Tamaño de la caché L3: {tamaño_cache}")

# Mostrar información de la caché L2
print("Información de la caché L2:")
Cache_2.obtener_informacion_cache()

# Preguntar al usuario si desea limpiar la caché del sistema
respuesta = input("¿Desea limpiar la caché del sistema? (s/n): ").lower()
if respuesta == 's':
    try:
        ctypes.windll.kernel32.SetSystemFileCacheSize(-1, -1, 0)
        print("Caché del sistema eliminada exitosamente.")
    except Exception as e:
        print(f"Error al intentar eliminar la caché del sistema: {e}")