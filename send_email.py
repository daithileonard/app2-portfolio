import smtplib, ssl
import os



EMAIL = {EMAIL}
PASSWORD = {PASSWORD}

def send_email(message_local):
    host = "smtp.gmail.com"
    port = 465
    username = EMAIL
    # password = os.getenv("PASSWORD")
    password = PASSWORD
    receiver = EMAIL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_local)
