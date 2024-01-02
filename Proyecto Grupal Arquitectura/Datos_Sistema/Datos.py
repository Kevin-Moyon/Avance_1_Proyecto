import psutil
import cpuinfo
import subprocess

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

def mostrar_datos_sistema():
    memoria_disponible = psutil.virtual_memory().available / (1024 * 1024)
    memoria_usada = psutil.virtual_memory().percent
    rendimiento_red = psutil.net_io_counters().bytes_sent / (1024 * 1024)

    try:
        temperatura_cpu = psutil.sensors_temperatures()['coretemp'][0].current
    except AttributeError:
        temperatura_cpu = "No disponible en esta plataforma"

    info_cpu = cpuinfo.get_cpu_info()
    tamaño_cache = obtener_tamano_cache()

    # Obtener la carga actual de la CPU
    rendimiento_cpu = psutil.cpu_percent()

    print(f"\nRendimiento de la CPU: {rendimiento_cpu}%")
    print(f"\nMemoria disponible: {memoria_disponible:.2f} MB")
    print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
    print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
    print(f"Temperatura del CPU: {temperatura_cpu}")
    print(f"Información de la CPU: {info_cpu}")
    print(f"Tamaño de la caché L3: {tamaño_cache}")

if __name__ == "__main__":
    mostrar_datos_sistema()

