
from VisualizingResults.Visualizer import Visualizer
from EmailProcedures.utils import group_uni_emails

# Visualizer.visualize_university_email_numbers(True)

from EmailProcedures.ParsingAndSavingEmails import count_all_emails
w = count_all_emails()
print(group_uni_emails(w))