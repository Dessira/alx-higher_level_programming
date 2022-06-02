#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    var = len(sys.argv)
    if var == 1:
        print("0 arguments.")
    elif var == 2:
        print("{:d} argument:".format(var - 1))
    else:
        print("{:d} arguments:".format(var - 1))
    for i in range(1, var):
        print("{:d}: {:s}".format(i, sys.argv[i]))
