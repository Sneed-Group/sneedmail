from __future__ import print_function
from datetime import datetime
import asyncore
from smtpd import SMTPServer
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

email_server = False



def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def crypter(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        f = open(filename, 'w')
        f.write(crypter(data))
        f.close
        print('%s saved.' % filename)
        self.no += 1

def EmlClientSend(sender, to, subject, msg, passwd, server, port):
    mail_client = smtplib.SMTP(server, port)
    mail_client.ehlo()
    mail_client.login(sender, crypter(passwd))
    messg = MIMEMultipart()
    messg['From'] = sender
    messg['To'] = to
    messg['Subject'] = subject
    message = msg
    messg.attach(crypter(MIMEText(message)))
    mail_client.sendmail(sender, to, messg)

def run_server():
    # start the smtp server on localhost:1025
    email_server = EmlServer(('localhost', 1025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

def run_client():
    while True:
        server = "<Mail server>: "
        port = "<Port>: "
        sender = input("<Sender Address>: ")
        passwd = crypter(input("<Sender Password>: "))
        to = input("<To>: ")
        subject = input("<Subject>: ")
        msg = input("<Message>: ")
        try:
            EmlClientSend(sender, to, subject, msg, crypter(passwd), server, port)
            print("OK")
        except:
            print("Error!")
if __name__ == '__main__':
    run_client()
