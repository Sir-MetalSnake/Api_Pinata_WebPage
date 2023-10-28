from datetime import *
import smtplib
from email.mime.text import MIMEText
import random
import hashlib
import string
from fastapi import HTTPException

char = (string.digits + string.
        ascii_letters + string.punctuation)

from MyTables.secret_key import *


class Sender:
    Email_sender = ''
    sender_password = ''

    def __init__(self, Email_sender, sender_password):
        self.Email_sender = Email_sender
        self.sender_password = sender_password

    def Send_Mail(self, subject, receiver, file, code):
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


async def Send_Mail_Code_Verify(user):
    cli = usuario_cliente.select().where(usuario_cliente.usuario == user)
    sender = Sender("ansirkhziur@gmail.com", "diyv behc uqqm tydq")  # en esta parte llamamos a la clase Sender
    # Se crea de forma automatica el codigo para conectarse
    p1 = ''.join(random.choice(char) for i in range(3))
    p2 = ''.join(random.choice(char) for i in range(3))
    p3 = ''.join(random.choice(char) for i in range(3))
    code = p1 + '-' + p2 + '-' + p3  # o63-948-eu3
    sender.Send_Mail(subject="Cambio de Contraseña", receiver=cli.Correo, file="res/Recovery_pass.html",
                     code=code)  # Hacemos llamado a la funcion
    h1 = hashlib.sha512(code.encode()).hexdigest()
    t = datetime.utcnow() + timedelta(minutes=3)
    print(t)
    secret_key.create(Key_name=h1, Id_usuario=cli.idusuarios, Expire=t)
    return "Email Send Sucessfully"


async def Compare_Secret_Key(Key):
    loki = datetime.utcnow()
    cypher = hashlib.sha512(Key.encode()).hexdigest()
    valhalla = secret_key.select().where(secret_key.KeyName == cypher and loki <= secret_key.Expire)
    if valhalla:
        return True
    else:
        raise HTTPException(404, 'El código no coincide o Ya Expiro')