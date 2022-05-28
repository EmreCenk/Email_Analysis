
# Importing libraries
import os
from SavingEmails import load_email
import email
from pprint import pprint
print = pprint
for k in os.listdir("Emails"):
    arr = load_email(k)[1][0]
    msg = email.message_from_string(str(arr[1], 'utf-8'))
    for k in msg: print(k)
    # print((load_email(k)[1][0]))
    break