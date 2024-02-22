import ctypes


class CACHE_DESCRIPTOR(ctypes.Structure):
    _fields_ = [("Level", ctypes.c_byte),
                ("Associativity", ctypes.c_byte),
                ("LineSize", ctypes.c_ushort),
                ("Size", ctypes.c_ulong),
                ("Type", ctypes.c_int)]


def imprimir_pag_seg():
    # Tamaño requerido para el búfer
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION_SIZE = 128
    buffer = ctypes.create_string_buffer(SYSTEM_LOGICAL_PROCESSOR_INFORMATION_SIZE)
    bytes_returned = ctypes.c_ulong()

    success = ctypes.windll.kernel32.GetLogicalProcessorInformation(buffer, ctypes.byref(bytes_returned))

    if success == 0 and ctypes.windll.kernel32.GetLastError() == 122:
        buffer = ctypes.create_string_buffer(bytes_returned.value)
        success = ctypes.windll.kernel32.GetLogicalProcessorInformation(buffer, ctypes.byref(bytes_returned))

    # Procesa la información de la caché
    if success != 0:
        offset = 0
        cache_info = []

        while offset + ctypes.sizeof(CACHE_DESCRIPTOR) <= bytes_returned.value:
            info = CACHE_DESCRIPTOR.from_buffer(buffer, offset)
            cache_info.append(info)
            offset += ctypes.sizeof(CACHE_DESCRIPTOR)

    if success != 0:
        offset = 0
        cache_info = {'L1': [], 'L2': [], 'L3': [], 'Otro': []}

        while offset + ctypes.sizeof(CACHE_DESCRIPTOR) <= bytes_returned.value:
            info = CACHE_DESCRIPTOR.from_buffer(buffer, offset)
            if info.Level == 1:
                cache_info['L1'].append(info)
            elif info.Level == 2:
                cache_info['L2'].append(info)
            elif info.Level == 3:
                cache_info['L3'].append(info)
            else:
                cache_info['Otro'].append(info)
            offset += ctypes.sizeof(CACHE_DESCRIPTOR)

        for level, caches in cache_info.items():
            print()
            print(f"Segmento de Caché {level}:")
            for index, cache in enumerate(caches):
                print(
                    f"  Cache {index + 1} - Size: {cache.Size / 1024} KB, Associativity: {cache.Associativity}, Line Size: {cache.LineSize} bytes")
                print()  # Agregar línea en blanco entre cada caché
            print()  # Agregar línea en blanco después de cada segmento de caché
    else:
        print(f"No se pudo obtener información de la caché. Código de error: {ctypes.windll.kernel32.GetLastError()}")


if __name__ == "__main__":
    imprimir_pag_seg()
