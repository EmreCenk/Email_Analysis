
# Importing libraries
import imaplib, email
from dotenv import load_dotenv
import os
load_dotenv()

#CONSTANTS:
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


GMAIL_ADRESS = os.environ["application_email_username"]
PASSWORD = os.environ["application_email_password"]
imap_url = 'imap.gmail.com'



mail = imaplib.IMAP4_SSL(SMTP_SERVER)

# if the following line gives an error, enable the following setting:
# https://myaccount.google.com/lesssecureapps?pli=1
mail.login(GMAIL_ADRESS, PASSWORD)
mail.select('inbox')

data = mail.search(None, 'ALL')
mail_ids = data[1]
id_list = mail_ids[0].split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

for i in range(latest_email_id, latest_email_id-3, -1):
    data = mail.fetch(str(i), '(RFC822)')
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_string(str(arr[1], 'utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print('From: ' + email_from + '\n')
            print('Subject: ' + email_subject + '\n')




