


def sort_dictionary_on_values(to_sort):
    return sorted(to_sort, key = lambda x: to_sort[x], reverse = True)

def group_uni_emails(dictionary):
    """
    Groups different email adresses to find which university they are coming from
    :param dictionary:
    :return:
    """

    #list of unis I applied to (and sent me emails):
    # "short form": "official name"
    unis = {"laurier": "Wilfrid Laurier University",
            "wlu": "Wilfrid Laurier University",

            "waterloo": "University of Waterloo",
            "toronto": "University of Toronto",
            "carleton": "Carleton University",
            "ryerson": "Ryerson University",
            "ottawa": "University of Ottawa",
            "mcmaster": "McMaster University",
            "queen": "Queen's University",
            "york": "York University",
            "alberta": "University of Alberta"}

    new_count = {}
    for k in unis: new_count[unis[k]] = 0

    for name in dictionary:
        asdf = True
        for uni in unis:
            if uni.lower() in name.lower():
                print(name, "->", unis[uni])
                new_count[unis[uni]] += dictionary[name]
                asdf = False
                break

        if asdf: print(name)
    return new_count