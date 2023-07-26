import smtplib
import ssl
from email.message import EmailMessage

from datetime import datetime

def geraWarning(message: str):
    smtp_port = 465
    smtp_server = 'smtp.gmail.com'
    email_from = 'nuvemalertas@gmail.com'
    pswd = 'phadzfsfablfxmwh'
    email_to = 'joaovsdo@algartech.com,'
    
    #'joaovictorsousadeoliveira345@gmail.com, joaovsdo@algartech.com, adrianosds@algartech.com, rafaelnsb@algartech.com'
    

    msg = EmailMessage()
    msg['Subject'] = 'Nuvem Sales Warning'
    msg['From'] = email_from
    msg['To'] = email_to
    msg.set_content(message)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:

        smtp.login(email_from, pswd)
        smtp.send_message(msg=msg)
        smtp.quit()
