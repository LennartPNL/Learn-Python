# Text messaging (Twilio)

from twilio.rest import Client

# Fill in your credentials here
# You should go to Twilio's website first, to sign up

# Your account's SID
accSID = ""

# Authentication token
authToken = ""

# Create a Twilio Client
twilioClient = Client(accSID, authToken)

# The number you get from Twilio
myTwilioNum = ""

# The number where you want to receive the SMS
myNum = ""

# Sending the message
message = twilioClient.messages.create(body="One new message", from_=myTwilioNum, to=myNum)


