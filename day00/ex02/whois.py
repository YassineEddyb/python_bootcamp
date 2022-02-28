from sys import argv

count = len(argv)
if (count <= 1):
    exit()

if (count > 2):
    print("AssertionError: argument is not an integer")
    exit()

str = argv[1]

if (str.isdecimal()):
    nbr = int(argv[1])
    if (nbr == 0):
        print("i'm Zero")
    elif (nbr % 2 == 0):
        print("i'm Even")
    else:
        print("i'm Odd")
else:
    print('AssertionError: more than one argument are provided')
