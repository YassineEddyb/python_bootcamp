from sys import argv

count = len(argv)

if (count > 2):
    print("AssertionError: more than one argument are provided")


def text_analyzer(text=None):
    if text is None:
        text = input("what is the text to analyze?\n>> ")

    if (type(text) != str):
        print("AssertionError: argument is not a string")
        return

    lower = 0
    upper = 0
    space = 0
    punc = 0
    num = 0

    for i in text:
        if(i.isupper()):
            upper += 1
        elif (i.islower()):
            lower += 1
        elif (i.isspace()):
            space += 1
        elif (i.isnumeric()):
            num += 1
        else:
            punc += 1

    sum = upper + lower + space + punc + num

    print(f"The text contains {sum} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punc} punctuation mark(s)")
    print(f"- {space} space(s)")


text_analyzer.__doc__ = "\n   This function counts the number of upper \
    characters,lower characters, \npunctuation and spaces in a given text.\n"

if (count == 2):
    text_analyzer(argv[1])
