from datetime import *
import smtplib
from email.mime.text import MIMEText
import random
import hashlib
import string
from fastapi import HTTPException

from MyTables.secret_key import *

class Sender:
    Email_sender = ''
    sender_password = ''

    def __init__(self,Email_sender,sender_password):
        self.Email_sender = Email_sender
        self.sender_password = sender_password

    def Send_Mail(self,subject,receiver,file, code):
        Myfile = open(file, "r", encoding="utf-8")
        readFile = Myfile.read()
        readFile = readFile.replace("MI_CODE", code)
        readFile = readFile.replace("MI_CORREO", receiver)
        msg = MIMEText(readFile, 'html')
        msg['Subject'] = subject
        msg['From'] = self.Email_sender
        msg['To'] = receiver
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
            mail.login(self.Email_sender, self.sender_password)
            mail.sendmail(self.Email_sender, receiver, msg.as_string())

async def SendMAil_User(user):
    cli = usuario_cliente.select().where(usuario_cliente.usuario == user)



# diyv behc uqqm tydq
# async def Verification_Email():
#     return True
#
#
# class emailSend:
#     sender = ""
#     password = ""
#
#     def __init__(self, sender, password):
#         self.sender = sender
#         self.password = password

    # def sendM(self, subject, receiver, file, code):
    #     Myfile = open('res/Recovery_pass.html', "r", encoding="utf-8")
    #     readFile = Myfile.read()
    #     readFile = readFile.replace("MI_CODE", '2932011')
    #     readFile = readFile.replace("MI_CORREO", correo)
    #     msg = MIMEText(readFile, 'html')
    #     msg['Subject'] = subject
    #     msg['From'] = self.sender
    #     msg['To'] = self.password
    #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
    #         mail.login(self.sender, self.password)
    #         mail.sendmail(self.sender, receiver, msg.as_string())
    #
    #     return "Email Send Sucessfully"
