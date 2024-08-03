import random
import string

# Funktion zur Generierung einer zufälligen Zeichenfolge
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Erstellung einer temporären E-Mail-Adresse
temp_email_local = generate_random_string()
temp_email_domain = 'example.com'  # Ersetze dies durch eine echte temporäre E-Mail-Domain
temp_email = f"{temp_email_local}@{temp_email_domain}"
print(f"Generierte temporäre E-Mail-Adresse: {temp_email}")

# Benutzerdefinierte E-Mail-Adresse
receiver_email = input("Geben Sie die Ziel-E-Mail-Adresse ein: ")

# E-Mail-Inhalt
subject = input("Geben Sie den Betreff der E-Mail ein: ")
body = input("Geben Sie den Text der E-Mail ein: ")

# E-Mail-Konfiguration
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = temp_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# SMTP-Server-Informationen
smtp_server = 'smtp.gmail.com'  # Beispiel: Gmail SMTP-Server
smtp_port = 587
smtp_user = 'your_smtp_user'  # E-Mail zum Senden
smtp_password = 'your_smtp_password'  # Passwort für den SMTP-Server

# Senden der E-Mail
import smtplib

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # TLS verwenden
    server.login(smtp_user, smtp_password)
    server.send_message(msg)
    print("E-Mail erfolgreich gesendet!")
except Exception as e:
    print(f"Fehler beim Senden der E-Mail: {e}")
finally:
    server.quit()
