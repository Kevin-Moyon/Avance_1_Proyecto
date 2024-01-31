import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp-mail.outlook.com"
port = 587
sender_email = "kevincitojoel@outlook.es"
password = "k3v1nj03l"

def conectar_smtp():
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    return server

def desconectar_smtp(server):
    server.quit()

def enviar_correo(sender_email, correo_destinatario, archivo_html, nombre_archivo_adjunto="Localizacion.html"):
    server = conectar_smtp()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = correo_destinatario
    message["Subject"] = "LOCALIZACION "
    body = "Abre la página web para comprobar si tu ubicación, esta dentro o fuera de la zona planteada."
    message.attach(MIMEText(body, "plain"))

    with open(archivo_html, "r", encoding="utf-8") as file:
        html_content = file.read()
        html_attachment = MIMEText(html_content, "html")
        html_attachment.add_header('Content-Disposition', 'attachment', filename=nombre_archivo_adjunto)
        message.attach(html_attachment)

    try:
        server.sendmail(sender_email, correo_destinatario, message.as_string())
        print("Correo electrónico enviado exitosamente!")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")
    finally:
        desconectar_smtp(server)