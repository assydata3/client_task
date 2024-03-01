import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = 'assydata@minebea-as.com'
sender_pass = 'hondalock@123'
class mailer:
    def sent_mail_1(sent_to,mail_title,mail_body):
        message = MIMEMultipart()
        sender = sender_address
        message['From']= sender
        message['To']= sent_to
        message['Subject'] = mail_title
        message.attach(MIMEText(mail_body, 'plain'))
        session = smtplib.SMTP('smtp.office365.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address,sent_to, text)
        session.quit()
        print('finish request mail !')


    def sent_mail_multi(sent_to,sent_cc,title,content):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = sent_to
        message['Cc'] = sent_cc
        message["Subject"] = title
        message.attach(MIMEText(content, 'html'))
        session = smtplib.SMTP('smtp.office365.com', 25)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, message["To"].split(",") + message["Cc"].split(","), text)
        session.quit()
        print('Mail Sent')

# mailer.sent_mail_1('tung_phung@minebea-as.com','test mail','test thu xem phat the nao')
mailer.sent_mail_multi('tung_phung@minebea-as.com','itechcolor1984@gmail.com','test','test xem thu the nao')