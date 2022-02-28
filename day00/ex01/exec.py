import sys

count = len(sys.argv)
if (count <= 1):
    exit()

str = sys.argv[1]
i = 2

while (i < count):
    str += ' ' + sys.argv[i]
    i += 1

print(str[::-1])
