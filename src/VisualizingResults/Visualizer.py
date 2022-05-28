

from src.EmailProcedures.ParsingAndSavingEmails import count_all_emails
from src.EmailProcedures.utils import sort_dictionary_on_values
import matplotlib.pyplot as plt

class Visualizer():

    @staticmethod
    def visualize_university_email_numbers(group_emails: bool = False):
        """
        :param group_emails: If you want to group similar emails
        Ex: "waterlooadmissions@gmail.com" and "universityofwaterloo@gmail.com" would go under
        "University of Waterloo"
        :return:
        """

        email_count = count_all_emails()
        sorted = sort_dictionary_on_values(email_count)
        uni_names = []
        values = []
        for name in sorted:
            # if email_count[name] < 10: break
            uni_names.append(name)
            values.append(email_count[name])

        plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(uni_names, values, color='maroon', width=0.4)

        plt.xlabel("University Name")
        plt.ylabel("Number of Emails Sent")
        plt.title("Students enrolled in different courses")
        plt.show()
