import email, smtplib, ssl
import csv
import getpass
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendBulkMail(sender_mail_id,sender_password,smtp_address,smtp_port,subject,message):
    csvfile = str(input("name / path of CSV File containing EmailIds of reciver with extension"))
    mail_address = []

    try:
        with open(csvfile,mode='r') as send_list:
            csv_reader = csv.reader(csvfile,delimiter=',')
            for row in csv_reader:
                for mail in row:
                    mail_address.append(mail)
            send_list.close()

    except FileNotFoundError as identifier:
        print(identifier.strerror)
    
    mimeMessage = MIMEMultipart()
    mimeMessage["From"] = sender_mail_id
    mimeMessage["To"] = ','.join(mail_address)
    mimeMessage["Subject"] = subject
    mimeMessage.attach(MIMEText(message,'plain'))
    mail_message = mimeMessage.as_string()

    mServer = smtplib.SMTP(host=smtp_address,port=smtp_port)
    mServer.starttls()

    try:
        mServer.login(user=sender_mail_id,password=sender_password)
        mServer.sendmail(sender_mail_id,mail_address,mail_message)
        print("mail Sent Successfully !")
        mServer.quit()
    except smtplib.SMTPException as identifier:
        print(identifier.strerror)
        print("Failed to Send Bulk Mail !")
        mServer.quit()

if __name__ == "__main__":
    sender_email = str(input("Enter your Email Id :"))
    sender_password = getpass.getpass("Enter yor Password (Your password will be hidden for security purpose ) :")
    reciver_email = str(input("Enter to Whom do you want to send Email :"))
    domain = sender_email[sender_email.index("@")+1:sender_email.index(".")]
    smtp_address = str(input("Enter the SMTP Address for "+str(domain)+" :"))
    smtp_port = int(input("Enter the SMTP Port Number for "+str(domain)+" :"))
    subject_mail = str(input("Enter the Subject :"))
    body_mail = str(input("Enter the Message :"))
    sendBulkMail(sender_mail_id=sender_email,sender_password=sender_password,smtp_address=smtp_address,smtp_port=smtp_port,subject=subject_mail,message=body_mail)