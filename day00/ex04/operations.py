from sys import argv

count = len(argv)
if (count <= 2):
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n   python operations.py 10 3")
    exit()

if (count > 3):
    print("AssertionError: too many arguments")
    exit()

if (argv[1].isnumeric() is False or argv[2].isnumeric() is False):
    print("AssertionError: only integers")
    exit()

a = int(argv[1])
b = int(argv[2])

print(f"sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
if (b == 0):
    print("Quotient: ERROR (division by zero)")
else:
    print(f"Quotient: {a / b}")

if (b == 0):
    print("Remainder: ERROR (modulo by zero)")
else:
    print(f"Remainder: {a % b}")
