import string
cleveland_data = open("cleveland_data.txt", "r")

def create_list():
    patient_list = []
    item_list = []
    for line in cleveland_data:
        if len(item_list) != 0 and item_list[-1] == "name":
            patient_list.append(item_list)
            item_list = []
        for item in line.split():
            item = item.strip(string.whitespace)
            item_list.append(item)
    patient_list.append(item_list)
    return patient_list

cleveland = create_list()
# The last patient doesn't 76 attributes. Pop.
cleveland.pop()
