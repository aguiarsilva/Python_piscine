import sys

def checkNum(num: int):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

try:
    n = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not integer")

checkNum(n)
