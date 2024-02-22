import psutil


def get_process_info():
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            process_id = process.info['pid']
            process_name = process.info['name']
            # Obtener el uso de CPU para todos los núcleos
            cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
            # Seleccionar el valor correspondiente al proceso actual
            process_cpu_percent = cpu_percentages[process_id % psutil.cpu_count()]

            process_memory_info = process.info['memory_info']

            print("ID de proceso:", process_id)
            print("Nombre:", process_name)
            print("Uso de CPU (%):", process_cpu_percent)
            print("Uso de memoria (bytes):", process_memory_info.rss)
            print("-" * 30)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    get_process_info()

