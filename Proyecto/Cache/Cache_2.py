import ctypes

class CACHE_DESCRIPTOR(ctypes.Structure):
    _fields_ = [("Level", ctypes.c_byte),
                ("Associativity", ctypes.c_byte),
                ("LineSize", ctypes.c_ushort),
                ("Size", ctypes.c_ulong),
                ("Type", ctypes.c_int)]

def obtener_informacion_cache():
    # Intentar obtener el tamaño requerido para el búfer
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_SIZE = 128
    buffer = ctypes.create_string_buffer(SYSTEM_LOGICAL_PROCESSOR_INFORMATION_SIZE)
    bytes_returned = ctypes.c_ulong()

    success = ctypes.windll.kernel32.GetLogicalProcessorInformation(buffer, ctypes.byref(bytes_returned))

    if success == 0 and ctypes.windll.kernel32.GetLastError() == 122:
        buffer = ctypes.create_string_buffer(bytes_returned.value)
        success = ctypes.windll.kernel32.GetLogicalProcessorInformation(buffer, ctypes.byref(bytes_returned))

    # Procesar la información de la caché
    if success != 0:
        offset = 0
        cache_info = []

        while offset + ctypes.sizeof(CACHE_DESCRIPTOR) <= bytes_returned.value:
            info = CACHE_DESCRIPTOR.from_buffer(buffer, offset)
            cache_info.append(info)
            offset += ctypes.sizeof(CACHE_DESCRIPTOR)

        for index, cache in enumerate(cache_info):
            print(f"Cache {index + 1} - Level: {cache.Level}, Size: {cache.Size / 1024} KB, Associativity: {cache.Associativity}, Line Size: {cache.LineSize} bytes")
    else:
        print(f"No se pudo obtener información de la caché. Código de error: {ctypes.windll.kernel32.GetLastError()}")

# Agregar la siguiente línea para evitar que se imprima automáticamente al importar el módulo
if __name__ == "__main__":
    # Llamar a la función solo si el script se ejecuta directamente
    obtener_informacion_cache()
