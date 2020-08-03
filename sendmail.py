import mail_module
import getpass

if __name__ == '__main__':
    print("Select the Mailing Type \n")
    print(" 1. Send Email (single Mail)\n 2. Send Bulk Email (using csv file) \n")
    selected_option = int(input("Your Option (1 or 2) press ctrl +c to exit \n"))

    sender_email = str(input("Enter your Email Id :"))
    sender_password = getpass.getpass("Enter yor Password (Your password will be hidden for security purpose ) :")
    #Gmail smtp address : smtp.gmail.com
    #Gmail port address : 587
    domain = sender_email[sender_email.index("@")+1:sender_email.index(".")]
    smtp_address = str(input("Enter the SMTP Address for "+str(domain)+" :"))
    smtp_port = int(input("Enter the SMTP Port Number for "+str(domain)+" :"))

    if selected_option == 1:
        reciver_email = str(input("Enter to Whom do you want to send Email :"))
        subject_mail = str(input("Enter the Subject :"))
        body_mail = str(input("Enter the Message :"))
        mail_module.sendMail(smtp_address=smtp_address,smtp_port=smtp_port,sender_address=sender_email,reciver_email=reciver_email,sender_pswrd=sender_password,subject=subject_mail,message=body_mail)

    if selected_option == 2:
        subject_mail = str(input("Enter the Subject :"))
        body_mail = str(input("Enter the Message :"))
        mail_module.sendBulkMail(sender_mail_id=sender_email,sender_password=sender_password,smtp_address=smtp_address,smtp_port=smtp_port,subject=subject_mail,message=body_mail)

