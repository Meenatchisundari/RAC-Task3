import csv
import smtplib
from email.message import EmailMessage
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
try:
 server.login('gmail.com','password')
except Exception as e:
 print(e)
subject='RAC'
msg='''Hello\n
This is my check mail through Python Program.\n

Regards\n
Meenatchi'''
sender='meenadharshini0407@gmail.com'

with open("C:/Users/ASUS/OneDrive/Documents/Python problems/Mail.csv") as file:
    reader=csv.reader(file)
    next(reader)
    for name,addr,content in reader:
        email=EmailMessage()
        email['From']=sender
        email['To']=addr
        email['Subject']=subject
        email.set_content(content)
        server.send_message(email)
server.close
