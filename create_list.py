import string

def create_list(data):
    patient_list = []
    item_list = []
    for line in data:
        if len(item_list) != 0 and item_list[-1] == "name":
            patient_list.append(item_list)
            item_list = []
        for item in line.split():
            item = item.strip(string.whitespace)
            item_list.append(item)
    # If a patient's data doesn't have 76 elements(including NULL),
    # do not include it into the patient_list.
    if len(item_list) == 76:
        patient_list.append(item_list)
    return patient_list
