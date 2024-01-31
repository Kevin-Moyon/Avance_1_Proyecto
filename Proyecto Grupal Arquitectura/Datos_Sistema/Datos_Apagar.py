import psutil
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PID_Barra_Tareas.Anlisis_PID import obtener_procesos_en_ejecucion
from Cache.Datos_Cache import obtener_informacion_cache  # Asegúrate de cambiar 'tu_archivo' al nombre real de tu archivo

def obtener_porcentaje_rendimiento():
    # Obtener la carga actual de la CPU
    rendimiento_cpu = psutil.cpu_percent(interval=1)
    return rendimiento_cpu

def enviar_correo(destinatario, razon):
    servidor_correo = "smtp.live.com"
    puerto_correo = 587
    usuario_correo = "cnff001@hotmail.com"
    contraseña_correo = "Cuentanueva2023"

    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_correo
    mensaje['To'] = destinatario
    mensaje['Subject'] = "Alerta de Apagado del CPU"

    cuerpo_mensaje = f"El CPU se apagó debido a la siguiente razón:\n\n{razon}"
    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    with smtplib.SMTP(servidor_correo, puerto_correo) as servidor:
        servidor.starttls()
        servidor.login(usuario_correo, contraseña_correo)
        servidor.send_message(mensaje)

def apagar_si_rendimiento_excede_limite(limite, destinatario):
    rendimiento_actual = obtener_porcentaje_rendimiento()

    procesos_en_ejecucion = obtener_procesos_en_ejecucion()

    if rendimiento_actual > limite:
        razon_apagado = f"El rendimiento ha excedido el {limite}%. Apagando el sistema...\n"
        razon_apagado += "Procesos en ejecución:\n"
        for proceso in procesos_en_ejecucion:
            razon_apagado += f"Process ID: {proceso['pid']}, Nombre: {proceso['nombre']}\n"

        # Llama a la función para obtener información de la caché y guárdala en la variable 'razon'
        razon = obtener_informacion_cache()
        print(razon_apagado)
        enviar_correo(destinatario, razon_apagado)
        os.system("shutdown /s /t 3")  # 3 segundos para que se apague

def rendimiento():
    rendimiento_cpu = obtener_porcentaje_rendimiento()
    print(f"\nRendimiento de la CPU: {rendimiento_cpu}%")
    print(f"\nEl dispositivo se apagará si el rendimiento de la CPU que ahora es: {rendimiento_cpu}%, excede el 90% de rendimiento.")

if __name__ == "__main__":
    destinatario = input("Ingrese el correo electrónico del dueño de la PC (Hotmail/Outlook): ")
    apagar_si_rendimiento_excede_limite(90, destinatario)
    rendimiento()
