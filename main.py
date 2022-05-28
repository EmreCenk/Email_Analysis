
# Importing libraries
from ParsingAndSavingEmails import parse_and_loop_all_emails
from collections import defaultdict
counted_emails = 0

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
    counted_emails += 1

from pprint import pprint
pprint(emails)
