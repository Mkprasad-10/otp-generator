import email, smtplib, ssl
import getpass
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(smtp_address,smtp_port,sender_address,sender_pswrd,reciver_email,subject,message):
    MimeMessage = MIMEMultipart()
    MimeMessage["From"] = sender_address
    MimeMessage["To"] = reciver_email
    MimeMessage["Subject"] = subject
    MimeMessage.attach(MIMEText(message,"plain"))
    mail_message = MimeMessage.as_string()
    mServer = smtplib.SMTP(host=smtp_address,port=smtp_port)
    mServer.starttls()

    try:
        mServer.login(user=sender_address,password=sender_pswrd)
        mServer.sendmail(sender_address,reciver_email,mail_message)
        print("Mail sent Successfully to "+ str(reciver_email))
        mServer.quit()
    except smtplib.SMTPException as identifier:
        print(identifier.strerror)
        print("Mail not sent !")
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
    sendMail(smtp_address=smtp_address,smtp_port=smtp_port,sender_address=sender_email,reciver_email=reciver_email,sender_pswrd=sender_password,subject=subject_mail,message=body_mail)