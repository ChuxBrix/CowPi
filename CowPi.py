#libraries
import gpiozero
import time
import smtplib

#define button
button = gpiozero.Button(2)

#store email variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'chestercowpi@gmail.com'
GMAIL_PASSWORD = 'CowsNeedWater2'

#email function
class Emailer:
    def sendmail(self, recipient, subject, content):
        #create headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        #connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        
        #login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        #send email and exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
#email function      
sender = Emailer()

#Check ever X amount of seconds and email status
while True:
    if button.is_pressed:
        sendTo = 'chestercowpi@gmail.com'
        emailSubject = "Water Level is NORMAL"
        emailContent = "All your drinks are belong to cows. " + time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Water Normal, E-Mail Sent " + time.ctime())
        el = open("EmailLog.txt", "a+")
        el.write(time.ctime() + " Sent WET Email \n")
        el.close()
        print("LOG: WET EMAIL")
        time.sleep(15000)
    else:
        sendTo = 'chestercowpi@gmail.com'
        emailSubject = "Cows are THIRSTY"
        emailContent = "These pretzels are making the cows thirsty!!! Low level detected: " + time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Water LOW, E-Mail Sent " + time.ctime())
        el = open("EmailLog.txt", "a+")
        el.write(time.ctime() + " Sent THIRSTY Email \n")
        el.close()
        print("LOG: THIRSTY EMAIL")
        time.sleep(15000)