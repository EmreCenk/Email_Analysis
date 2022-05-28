
# Importing libraries
import os
import pickle








def pickle_email(data):
    file = open(f"Emails/email_{len(os.listdir('Emails'))}", "ab")
    pickle.dump(data, file)
    file.close()

def load_email(file_name):
    file = open(f"Emails/{file_name}", 'rb')
    new_data = pickle.load(file)
    file.close()