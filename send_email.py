import smtplib
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 587

    user = "rontolero628@gmail.com"
    password = os.getenv("PASSWORD")
    #password = os.environ.get("PASSWORD")

    receiver = "rontolero628@gmail.com"

    server = smtplib.SMTP(host, port)
    server.starttls()

    server.login(user=user, password=password)
    server.sendmail(user, receiver, message)
