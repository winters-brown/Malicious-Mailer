"""
Author: Joshua Winters-Brown
emailer.py (c) 2021
Description: Send Malicious HTML Emails
Created:  2021-04-23T12:18:02.685Z
"""
#!/usr/bin/env python3
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

enviroment = open('enviroment.txt').readlines()
for line in enviroment:
    contents = line.split("=")
    if (contents[0] == 'EMAIL'):
        EMAIL = contents[1].strip()
    if (contents[0] == 'PASSWORD'):
        PASSWORD = contents[1].strip()

print(EMAIL)
print(PASSWORD)


emailServer = None
try:
    emailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    emailServer.login(EMAIL, PASSWORD)
except:
    print("Could not connect to email server")

sender = "yourmomscool@unorthodox.com"
reciever = "2693596699@mymetropcs.com"

# Create message container - the correct MIME type is multipart/alternative.
contents = MIMEMultipart('alternative')
contents['Subject'] = "Hello World"
contents['From'] = sender
contents['To'] = reciever

html = open('emails\hideExternal.html').read()
mimedHTML = MIMEText(html, 'html')
contents.attach(mimedHTML)


emailServer.sendmail(sender, reciever, str(contents))
emailServer.quit()
