

from src.EmailProcedures.ParsingAndSavingEmails import count_all_emails
from src.EmailProcedures.utils import sort_dictionary_on_values
import matplotlib.pyplot as plt
from src.EmailProcedures.utils import group_uni_emails

font = {
        # 'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 21
       }

plt.rc('font', **font)
class Visualizer():

    @staticmethod
    def visualize_university_email_numbers(group_emails: bool = True):
        """
        :param group_emails: If you want to group similar emails
        Ex: "waterlooadmissions@gmail.com" and "universityofwaterloo@gmail.com" would go under
        "University of Waterloo"
        :return:
        """

        email_count = count_all_emails()
        if group_emails:
            email_count = group_uni_emails(email_count)
        sorted = sort_dictionary_on_values(email_count)
        uni_names = []
        values = []
        for name in sorted:
            # if email_count[name] < 10: break
            uni_names.append(name.replace(" ", "\n"))
            values.append(email_count[name])

        plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(uni_names, values, color='maroon', width=0.4)

        # plt.xlabel("University Name")
        plt.ylabel("Number of Emails Sent")
        plt.title("Emails Sent By Universities")
        plt.show()
