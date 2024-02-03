import smtplib, ssl

# def send_email(message):
host = "smtp.gmail.com"
port = 465

username = "rontolero628＠gmail.com"
password = "tktgvhqwphiyogdp"

receiver = "rontolero628@gmail.com"
my_context = ssl.create_default_context()

message = """Hi there"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

