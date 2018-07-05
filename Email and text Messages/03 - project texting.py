# Sending SMS from a function

from twilio.rest import Client

# Fill in your credentials

accSID = ""
authToken = ""
myTwilioNum = ""
myNum = ""


def textMessage(message):
    twilioClient = Client(accSID, authToken)
    twilioClient.messages.create(body=message, from_=myTwilioNum, to=myNum)

while True:
    print()
    print("Press q to quit")
    print("Enter your message: ")
    userInput = str(input())
    if userInput == "q":
        print("See ya!")
        break
    else:
        textMessage(userInput)

    print("Your message '%s' is sent." % userInput)