#Solution problem number four:

def note_definitive(exam_1,exam_2,home_1,home_2,parti):
    note = (exam_1 * 0.2 
            + exam_2 * 0.4 
            + home_1 * 0.2 
            + home_2 * 0.2 
            + parti/10)
    return note


def classification(num_signature, definive):
    if num_signature == "FUNDAMENTOS":
        if definive >= 0 and definive < 2:
            return "MALO"
        elif definive >= 2 and definive < 3:
            return "DEFICIENTE"
        elif definive >= 3 and definive < 3.8:
            return "REGULAR"
        elif definive >= 3.8 and definive < 4.5:
            return "BUENO"
        else:
             return "EXCELENTE"
    if num_signature == "FUNDAMENTOS":
        if definive >= 0 and definive < 2:
            return "MALO"
        elif definive >= 2 and definive < 3:
            return "DEFICIENTE"
        elif definive >= 3 and definive < 3.8:
            return "REGULAR"
        elif definive >= 3.8 and definive < 4.5:
            return "BUENO"
        else:
             return "MALO"
    if num_signature == "FUNDAMENTOS":
        if definive >= 0 and definive < 2:
            return "MALO"
        elif definive >= 2 and definive < 3:
            return "DEFICIENTE"
        elif definive >= 3 and definive < 3.8:
            return "REGULAR"
        elif definive >= 3.8 and definive < 4.5:
            return "BUENO"
        else:
             return "MALO"
    if num_signature == "FUNDAMENTOS":
        if definive >= 0 and definive < 2:
            return "MALO"
        elif definive >= 2 and definive < 3:
            return "DEFICIENTE"
        elif definive >= 3 and definive < 3.8:
            return "REGULAR"
        elif definive >= 3.8 and definive < 4.5:
            return "BUENO"
        else:
             return "MALO"





menu =  """
WELCOME TO CALCULATE YOUR SCORE NOTE
UNIVERSIDAD DEL VALLE
"""


if __name__ == "___main__":
    print(menu)
    name = input("Enter your name: ")
    num_signature = input("Enter your signature: ").upper()
    exam_1 = float(input("Note exam 1: "))
    exam_2 = float(input("Note exam 2: "))
    home_1 = float(input("Note homework 1: "))
    home_2 = float(input("Note homework 2: "))
    parti = float(input("Note participate: "))
    definitive = note_definitive(exam_1,exam_2,home_1,home_2,parti)
    classification(num_signature, definitive)