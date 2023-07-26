# Import Packages For Email
from email.message import EmailMessage
import ssl
import smtplib


banner = """
   _______________          _______________
  |  ___________  |        |  ___________  |
  | |           | |        | |           | |
  | |   X   X   | |        | |           | |
  | |     -     | |        | |   0   0   | |
  | |    ___    | |        | |     -     | |
  | |   /   \   | |        | |   \___/   | |
  | |   \___/   | |        | |           | |
  | |___________| |        | |___________| |
  |_______________|        |_______________|
    ____|   |___.............._|________|_
   | ********** |            | ********** |
   | ********** |            | ********** |
    ------------              ------------
   [ Coded by: med-mahdi]
"""




#> Define The Function That Will Send The Email For Us
def sendingMail():
    email_sender = "youremail@gmail.com"
    # set the email_password to the password you generated from google Accounts, in the Security section 
    email_password = "app password"
    email_receiver = 'example@gmail.com'
    subject = "Hello sir, How are you Doing !"
    body = "This is a test Body Message."
    
    emailMessage = EmailMessage()
    emailMessage['From'] = email_sender
    emailMessage['To'] = email_receiver
    emailMessage['Subject'] = subject
    emailMessage.set_content(body)

    # Define Smtp connection
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, emailMessage.as_string())
        print("Message Sent Successfully!")


#> Call The Function
sendingMail()
