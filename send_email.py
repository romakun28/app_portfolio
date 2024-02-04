# import smtplib, ssl (this code was shown in the lesson but does not work. always show unocode　error)
#
# # def send_email(message):
# host = "smtp.gmail.com"
# port = 465
#
# user = "rontolero628＠gmail.com"
# password = "lnfsysmyzjkbpvkn"
#
# receiver = "rontolero628@gmail.com"
# my_context = ssl.create_default_context()
#
# message = "Hi There and Bye"
#
# with smtplib.SMTP_SSL(host, port, context=my_context) as server:
#     server.login(user, password)
#     server.sendmail(user, receiver, message)

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
