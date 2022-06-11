import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Mail sender name here'

email['to'] = 'first@gmail.com', 'second@gmail.com', 'third@gmail.com', 'fourth@gmail.com', 'fifth@gmail.com'

email['subject'] = 'Mail title here'

email.set_content('Mail content goes here')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'sendergmailpassword')
    smtp.send_message(email)
    print('Message sent, thanks')