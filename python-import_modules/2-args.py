#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # arqumentlər (argv[0] faylın adı)
    count = len(args)

    # Number of arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Print each argument
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
