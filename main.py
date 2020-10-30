# Email sender, using smtp library
# Enter your email address and password in EMAIL_ADDRESS and EMAIL_PASSWORD variables
# Currently, the code can only send image files

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# Currently the smtp is set for gmail                                                                                 #
# If you want to use this code you need to allow your gmail to be used by less secured apps (use non-main email)      #
# Log in to your email you will use and go to myaccount.google.com/lesssecureapps where you have to allow less secure #
# apps to use your email                                                                                              #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

import smtplib
import imghdr
from email.message import EmailMessage

# Enter your email address and password here
EMAIL_ADDRESS = 'your@email.com'
EMAIL_PASSWORD = 'your password'

# Enter emails you want to write to
contacts = ['example1@mail.com', 'example2@mail.com']

# Creating email message
msg = EmailMessage()
msg['Subject'] = 'Test subject'         # Enter your subject
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content("Testing")              # Enter your content

# Sending test photos
files = ['testfile1.png', 'testfile2.jpeg']

for file in files:
    with open(file, 'rb') as f:
        file_date = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_date, maintype='image', subtype=file_type, filename=file_name)

# Establishing connection with your gmail and sending the message
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
