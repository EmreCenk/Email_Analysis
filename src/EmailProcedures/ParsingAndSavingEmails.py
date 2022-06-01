

import pickle
import os
from src.EmailProcedures.FetchingEmails import EmailHandler
from src.EmailProcedures import utils
import email
from collections import defaultdict
from typing import Dict
from bs4 import BeautifulSoup

def pickle_email(data):
    file = open(f"Emails/email_{len(os.listdir('../Emails'))}", "ab")
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
    for k in os.listdir("./Emails"):
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

def get_uni_messages():
    emails = count_all_emails()
    email_count, grouped = utils.group_uni_emails(emails)
    uni_emails = set()
    for k in grouped:
        if k == "n/a": continue
        for w in grouped[k]: uni_emails.add(w)

    for msg in parse_and_loop_all_emails():
        try: email_source = msg["From"]
        except Exception as E: continue
        if email_source not in uni_emails: continue
        from time import sleep
        for part in msg.walk():
            yield str(part)

def count_words() -> Dict[str, int]:
    def zero(): return 0

    word_count = defaultdict(zero)

    for message in get_uni_messages():
        message = message.lower().replace(",", "").replace(".", "").replace("|", "")
        soup = BeautifulSoup(message, "html.parser")
        for word in soup.text.split(" "):
            word_count[word] += 1

    #
    from pprint import pprint
    i = 1
    final = {}
    for k in utils.sort_dictionary_on_values(word_count):
        if len(k) == 0: continue
        final[k[:100]] = word_count[k]
        if i > 20: break
        i+=1


    return final

