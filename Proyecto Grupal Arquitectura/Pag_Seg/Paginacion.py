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

def obtener_datos_sistema():
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

    # Almacenar los datos en una lista para facilitar la paginación
    datos = [
        f"Rendimiento de la CPU: {rendimiento_cpu}%",
        f"Memoria disponible: {memoria_disponible:.2f} MB",
        f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%",
        f"Rendimiento de la red: {rendimiento_red:.2f} MB",
        f"Temperatura del CPU: {temperatura_cpu}",
        f"Información de la CPU: {info_cpu}",
        f"Tamaño de la caché L3: {tamaño_cache}"
    ]

    return datos

def paginar_datos(datos, elementos_por_pagina):
    total_elementos = len(datos)
    paginas_totales = (total_elementos + elementos_por_pagina - 1) // elementos_por_pagina

    while True:
        try:
            print()
            numero_pagina = int(input(f"Ingrese el número de página (1-{paginas_totales}) o 0 para salir: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if numero_pagina == 0:
            break

        if 1 <= numero_pagina <= paginas_totales:
            inicio = (numero_pagina - 1) * elementos_por_pagina
            fin = min(numero_pagina * elementos_por_pagina, total_elementos)
            pagina_actual = datos[inicio:fin]

            print(f"\nPágina {numero_pagina}/{paginas_totales}:")
            for dato in pagina_actual:
                print(dato)
        else:
            print(f"El número de página debe estar entre 1 y {paginas_totales}.")

if __name__ == "__main__":
    # Obtener los datos del sistema
    datos_sistema = obtener_datos_sistema()

    # Ingresar la cantidad de elementos por página por teclado
    elementos_por_pagina = 3

    # Llamar a la función de paginación
    paginar_datos(datos_sistema, elementos_por_pagina)