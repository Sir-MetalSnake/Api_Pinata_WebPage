from datetime import *
import smtplib
from email.mime.text import MIMEText
import random
import hashlib
import string
from fastapi import HTTPException

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
