#una builtin funcion
from email.mime.text import MIMEText 
import smtplib

def enviacorre(email,altura,promedio_altura,cantidad):
    from_email="pythonwal77@gmail.com"
    from_password="Mpdepy33"
    to_email=email

    subject=" Datos de altura"
    message="Saludos, tu actual altura es <strong>%s</strong>. Y el promedio general de todos los usuarios es <strong>%s</strong>, de un total de <strong>%s</strong> usuarios " % (altura,promedio_altura,cantidad)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls() 
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

    