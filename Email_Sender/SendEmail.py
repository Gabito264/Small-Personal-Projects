from email.message import EmailMessage

import ssl
import smtplib

email_sender = '' #Email of the sender (in this case it's for gmail)
email_password= ''#Created Gmail password (top secret!)

email_receiver = ''#Email of receiver 
subject = "" #Subject (duh)
body= """

""" #Well, the text

em = EmailMessage()
em['From'] = email_sender
em['To']=email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

print("done!")