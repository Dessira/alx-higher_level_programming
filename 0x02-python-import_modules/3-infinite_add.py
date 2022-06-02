#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    var = len(sys.argv)
    if var == 1:
        print(0)
    else:
        for i in range(1, var):
            sum = sum + int(sys.argv[i])
        print("{:d}".format(sum))
