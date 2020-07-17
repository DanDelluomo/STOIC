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
    
    def send(self):
        display_string = principles.Stoic_Principles().display()
        print("SENDING: ", display_string)
        server_ssl.sendmail(self.username, self.username, 
                            display_string)

    def end_mailserver(self):
        #server_ssl.quit()
        server_ssl.close()









