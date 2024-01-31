import psutil


def obtener_procesos_en_ejecucion():
    procesos = []
    for proceso in psutil.process_iter(['pid', 'name']):
        procesos.append({
            'pid': proceso.info['pid'],
            'nombre': proceso.info['name']
        })
    return procesos


if __name__ == "__main__":
    procesos_en_ejecucion = obtener_procesos_en_ejecucion()

    print("Procesos en ejecución:")
    for proceso in procesos_en_ejecucion:
        print(f"Process ID: {proceso['pid']}, Nombre: {proceso['nombre']}")

