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

def run_client():
    while True:
        contents = input("<eMail Contents>: ")
        print(crypter(contents))

if __name__ == '__main__':
    run_client()
