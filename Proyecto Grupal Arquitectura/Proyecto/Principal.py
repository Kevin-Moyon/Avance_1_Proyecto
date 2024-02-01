import os
from Datos_Sistema.Datos import mostrar_datos_sistema
from Cache.Eliminar_Cache.Eliminar import mostrar_informacion_cache, borrar_cache
from Datos_Sistema.Datos_Apagar import apagar_si_rendimiento_excede_limite, rendimiento, enviar_correo
from PID_Barra_Tareas.Anlisis_PID import *
from Ubicacion.Ubi import enviar_correo , sender_email
from Localidades.Temporal import obtener_archivos_temporales
from Localidades.Espacial import obtener_archivos_espaciales
from Localidades.Secuencial import obtener_archivos_secuenciales

def mostrar_menu():
    correo_destinatario = None
    razon_apagado = None

    while True:
        print("\n------ Menú ------")
        print("1. Mostrar Datos del Sistema")
        print("2. Mostrar Información de la Caché")
        print("3. Mostrar Rendimiento actual")
        print("4. Mostrar Process ID")
        print("5. Enviar Correo Electrónico")
        print("6. Ubicación")
        print("7. Localidades")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            mostrar_datos_sistema()
        elif opcion == '2':
            razon_apagado = mostrar_informacion_cache()
            sub_menu_cache()
        elif opcion == '3':
            apagar_si_rendimiento_excede_limite(90, correo_destinatario)
            rendimiento()
        elif opcion == '4':
            mostrar_process_id()
            procesos_en_ejecucion = obtener_procesos_en_ejecucion()
            for proceso in procesos_en_ejecucion:
                print(f"Process ID: {proceso['pid']}, Nombre: {proceso['nombre']}")
        elif opcion == '5':
            print(f"\nIMPORTANTE: Ingresa tu correo de Outlook o Hotmail")
            correo_destinatario = input("Ingrese el correo electrónico del dueño de la PC: ")
            print(f"Tu correo {correo_destinatario} de propietario ha sido guardado con éxito.")
        elif opcion == '6':
            if correo_destinatario:
                print(f"Enviando correo a {correo_destinatario}...")
                print("...")
                enviar_correo(sender_email, correo_destinatario, "Localizacion.html")
            else:
                print("Primero debes ingresar el correo del propietario en la opción 5.")
        elif opcion == '7' :
            sub_menu_localidades()
        elif opcion == '8':
            print("")
            print("Gracias, por usar este sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    if correo_destinatario and razon_apagado:
        enviar_correo(correo_destinatario, razon_apagado)

def sub_menu_cache():
    while True:
        print("\n------ Submenú Caché ------")
        print("1. Borrar caché del sistema")
        print("2. Volver al menú principal")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            borrar_cache()
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def sub_menu_localidades():
    while True:
        print("\n------ Submenú Localidades ------")
        print("1. Localidad Temporal")
        print("2. Localidad Espacial")
        print("3. Localidad Secuencial")
        print("4. Volver al menú principal")

        sub_opcion = input("Ingrese el número de la opción deseada: ")

        if sub_opcion == '1':
            obtener_archivos_temporales()
            pass
        elif sub_opcion == '2':
            obtener_archivos_espaciales(os.getcwd())
            pass
        elif sub_opcion == '3':
            obtener_archivos_secuenciales(os.path.expanduser("~"))
            pass
        elif sub_opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def mostrar_process_id():
    pid = os.getpid()
    print(f"El ID de proceso es: {pid}")

if __name__ == "__main__":
    mostrar_menu()

