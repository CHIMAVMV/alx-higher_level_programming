#!/usr/bin/python3
import sys

# Get the list of arguments
args = sys.argv[1:]

# Print the number of arguments and the list of arguments
if len(args) == 0:
    print("No arguments.")
elif len(args) == 1:
    print("1 argument:")
    print(args[0])
else:
    print("{} arguments:".format(len(args)))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))



