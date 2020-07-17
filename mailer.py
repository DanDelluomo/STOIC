import principles 
import constants
import smtplib

class Email:
    """Send an email reminder of Stoic Principles every week."""

    def __init__(self):
        self.username = constants.username
        self.password = constants.password
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(self.username, self.password)
    
    def get_email_list(self):
        emails = []
        with open('email_list.txt', 'r') as f:
            for email in f.readlines():
                if '\n' in email:
                    email = email[:email.index('\n')]
                emails.append(email)
        return emails

    def send(self, email_list):
        display_string = principles.Stoic_Principles().display() 
        for address in email_list:
            print("SENDING TO: ", address)
            server_ssl.sendmail(self.username, address, display_string)
            
    def end_mailserver(self):
        #server_ssl.quit()
        server_ssl.close()









