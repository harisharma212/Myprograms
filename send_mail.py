import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(
    to_mail,
    subject,
    message,
    from_mail='h_sarma@ymail.com'
    ):
    """
    Method to send the email to specific mail_id includes,
    Subject, Message and etc.

    Args:
        to_mail(Mandatory): Mail to whoom to sent
        from_mail(dDefault): From mail to send
        subject (Default): Subject line
        message(Default): Message String
    """
    to_mail = to_mail if to_mail else "h.sarma212@gmail.com"
    subject = subject if subject else "TestMail"
    message = message if message else "This is a TestMail, sent though Python Code. :"
    
    print("Loading the credentials", end=' ')
    for i in range(5):
        print('*', end=' ')
        time.sleep(float(0.5))
    
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = subject
    message = message
    msg.attach(MIMEText(message))

    print("\nConnecting to Server. Please Wait", end=' ')
    for i in range(5):
        print('*', end=' ')
        time.sleep(float(0.25))
        
    mailserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    mailserver.ehlo()
    print("\nLogging into the Server. Please Wait", end=' ')
    for i in range(5):
        print('*', end=' '),
        time.sleep(float(0.5))
    
    mailserver.login('h_sarma@ymail.com', 'GhsKanna212$')
    print("\nLogin Success.. :)")
    print(f"Sending mail to {to_mail}")
    mailserver.sendmail('h_sarma@ymail.com',
                        to_mail,
                        msg.as_string()
                        )
    print(f"Message sent to {to_mail} successfully..")
    mailserver.close()

to_mail = str(input("Enter email address to send the mail: "))
subject = str(input("Enter the subject line: "))
message = str(input("Enter the message to be loaded:"))

sendmail(to_mail=to_mail, subject=subject, message=message)
