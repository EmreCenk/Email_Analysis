

import pickle
import os
from src.FetchingEmails import EmailHandler
import email
from collections import defaultdict
from typing import Dict

def pickle_email(data):
    file = open(f"src/Emails/email_{len(os.listdir('Emails'))}", "ab")
    pickle.dump(data, file)
    file.close()

def load_email(file_name):
    file = open(f"src/Emails/{file_name}", 'rb')
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


def count_all_emails() -> Dict[str, int]:
    # counted_emails = 0

    def zero(): return 0
    emails = defaultdict(zero)
    for msg in parse_and_loop_all_emails():
        try:
            email_source = msg["From"]
        except Exception as E:
            continue

        start = max(0, email_source.find("<") + 1)
        end = email_source.find(">")
        if end != -1: end += 1
        else: end = len(email_source)

        email_source = email_source[start: end]
        if (email_source == ""): print(msg["From"], start, end)
        emails[email_source] += 1
        # counted_emails += 1
    return emails