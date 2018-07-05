# SMTP and Emailing

import smtplib

# Connecting to your email address

# Connect to a SMTP server
smtpObject = smtplib.SMTP('smtp.gmail.com', 587)

# Saying hello to the server
print(smtpObject.ehlo())

# Using TLS encryption
print(smtpObject.starttls())

try:
    # Try logging in
    print(smtpObject.login("YOUREMAIL@gmail.com", "YOURPASSWORD"))
    # Try sending an email
    send = smtpObject.sendmail("YOUREMAIL@gamil.com", "YOURRECEPIANT@hotmail.com", "Subject: Hello John \n Hey Bob, You are a great big baffoon.")
    print(send)
except Exception as e:
    print(e)

# Closing the connection
print(smtpObject.quit())

# IMAP #

import imapclient

iObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)

iObj.login("YOUREMAIL@gmail.com", "YOURPASSWORD")

iObj.select_folder("INBAX", readonly=True)
UIDs = iObj.search(['SINCE 01-Jan-2018'])

print(UIDs)

rawMsg = iObj.fetch([UIDs[0]], ["BODY[]", "FLAGS"])

import pyzmail

msg = pyzmail.PyzMessage.factory(rawMsg[0]['BODY[]'])
msg.get_subject()







