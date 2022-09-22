#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    if num_arg = 1:
        print("{} argument:".format(num_arg -1)
    elif num == 2:
        print("{} argument:".format(num_arg - 1))
    else:
        print("{} arguments:".format(num_arg - 1))

    for i in range(1, num_arg):
        print("{}: {}".format(i, sys.argv[i]))
