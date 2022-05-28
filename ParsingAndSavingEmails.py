

import pickle
import os
from FetchingEmails import EmailHandler
import email
def pickle_email(data):
    file = open(f"Emails/email_{len(os.listdir('Emails'))}", "ab")
    pickle.dump(data, file)
    file.close()

def load_email(file_name):
    file = open(f"Emails/{file_name}", 'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data

def pickle_all_emails():
    emails = EmailHandler()
    for i, data in enumerate(emails.loop_through_email_data()):
        pickle_email(data)
        print(i)

def parse_and_loop_all_emails():
    for k in os.listdir("Emails"):
        arr = load_email(k)[1][0]
        try:
            msg = email.message_from_string(str(arr[1], 'utf-8'))
            yield msg
        except:
            yield None