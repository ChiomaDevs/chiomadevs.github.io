import sys


try:

    x = int(input("Enter the value of x: \n"))
    y = int(input("Enter the value  of y: \n"))

except ValueError:
    print("Error: Only integers should be entered.")
    sys.exit(1)

try:

    output = x / y

except ZeroDivisionError:
    print("Error: Non divisible by 0")
    sys.exit(1)

print(f"{x} / {y} = {output}")