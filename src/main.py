
# Importing libraries
from src.EmailProcedures.ParsingAndSavingEmails import count_all_emails
from src.EmailProcedures.utils import sort_dictionary_on_values

email_count = count_all_emails()
sorted = sort_dictionary_on_values(email_count)

for name in sorted:
    print(name, email_count[name])